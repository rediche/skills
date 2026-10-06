#!/usr/bin/env python3
"""Read session transcripts from OpenCode's local SQLite database."""

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_DB = Path.home() / ".local/share/opencode/opencode.db"


def connect(database: Path) -> sqlite3.Connection:
    if not database.is_file():
        raise FileNotFoundError(f"OpenCode database not found: {database}")
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def timestamp(milliseconds: int | None) -> str:
    if milliseconds is None:
        return "unknown time"
    return datetime.fromtimestamp(milliseconds / 1000, timezone.utc).astimezone().isoformat(timespec="minutes")


def list_sessions(connection: sqlite3.Connection, args: argparse.Namespace) -> None:
    filters = ["s.id <> ?"]
    values: list[str] = [args.exclude_session]
    if args.directory:
        filters.append("s.directory = ?")
        values.append(str(Path(args.directory).expanduser().resolve()))
    if args.project:
        filters.append("(p.name LIKE ? OR p.id = ? OR p.worktree = ?)")
        values.extend((f"%{args.project}%", args.project, args.project))
    where = f"WHERE {' AND '.join(filters)}" if filters else ""
    query = f"""SELECT s.id, s.title, s.directory, s.time_updated, p.name AS project
                FROM session s JOIN project p ON p.id = s.project_id
                {where} ORDER BY s.time_updated DESC LIMIT ?"""
    rows = connection.execute(query, [*values, args.limit]).fetchall()
    if not rows:
        print("No matching OpenCode sessions found.")
        return
    for row in rows:
        print(f"{row['id']}\t{timestamp(row['time_updated'])}\t{row['project'] or '-'}\t{row['directory']}\t{row['title']}")


def part_text(data: dict) -> str | None:
    kind = data.get("type")
    if kind == "text":
        return data.get("text", "")
    if kind == "tool":
        tool = data.get("tool", "tool")
        state = data.get("state", {})
        input_value = state.get("input") if isinstance(state, dict) else None
        return f"[Tool call: {tool}]" + (f"\n```json\n{json.dumps(input_value, indent=2, ensure_ascii=False)}\n```" if input_value is not None else "")
    if kind in {"image", "file", "compaction", "step-start", "step-finish", "reasoning"}:
        return None
    return None


def show_session(connection: sqlite3.Connection, session_id: str, excluded_session: str) -> None:
    if session_id == excluded_session:
        raise ValueError("Refusing to retrieve the session running this retrospective.")
    session = connection.execute(
        "SELECT id, title, directory, time_created FROM session WHERE id = ?", (session_id,)
    ).fetchone()
    if session is None:
        raise ValueError(f"Session not found: {session_id}")
    print(f"# {session['title']}\n\nSession: `{session['id']}`  \nDirectory: `{session['directory']}`  \nStarted: {timestamp(session['time_created'])}\n")
    messages = connection.execute(
        "SELECT id, data, time_created FROM message WHERE session_id = ? ORDER BY time_created, id",
        (session_id,),
    ).fetchall()
    for message in messages:
        try:
            metadata = json.loads(message["data"])
        except (TypeError, json.JSONDecodeError):
            metadata = {}
        role = metadata.get("role", "message")
        parts = connection.execute("SELECT data FROM part WHERE message_id = ? ORDER BY time_created, id", (message["id"],))
        content = []
        for row in parts:
            try:
                text = part_text(json.loads(row["data"]))
            except (TypeError, json.JSONDecodeError):
                text = None
            if text:
                content.append(text)
        if content:
            print(f"## {role.title()} — {timestamp(message['time_created'])}\n\n{'\n\n'.join(content)}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DB, help=f"SQLite database (default: {DEFAULT_DB})")
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="List recent sessions")
    listing.add_argument("--exclude-session", required=True, help="Session ID running this retrospective; it will be omitted")
    listing.add_argument("--directory", help="Filter by exact working directory")
    listing.add_argument("--project", help="Filter by project name, ID, or worktree")
    listing.add_argument("--limit", type=int, default=30, help="Maximum sessions to list (default: 30)")
    showing = commands.add_parser("show", help="Print a session transcript")
    showing.add_argument("session_id", help="Session ID from the list command")
    showing.add_argument("--exclude-session", required=True, help="Session ID running this retrospective; retrieval is refused for it")
    args = parser.parse_args()
    if args.command == "list" and args.limit < 1:
        parser.error("--limit must be at least 1")
    try:
        with connect(args.database) as connection:
            if args.command == "list":
                list_sessions(connection, args)
            else:
                show_session(connection, args.session_id, args.exclude_session)
    except (OSError, sqlite3.Error, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
