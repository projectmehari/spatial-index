#!/usr/bin/env python3
"""
check-arena.py — Fetch blocks from Are.na channel and diff against state.

This script fetches the channel and compares against .arena-last-seen.json.
When run by the cron agent, use --mark-seen to update state after processing.

The agent is responsible for:
  1. Running this script to detect new blocks
  2. For each new block with a URL: fetching article content (web_extract)
  3. Extracting structured funding data (LLM reasoning)
  4. Updating graph-data.js
  5. Committing + pushing
"""

import json
import os
import sys
import urllib.request
import urllib.error
import ssl

CHANNEL_SLUG = "world-models-funding"
API_URL = f"https://api.are.na/v3/channels/{CHANNEL_SLUG}/contents?per=100&sort=position_desc"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, "..", ".arena-last-seen.json")


def fetch_blocks() -> list[dict]:
    """Fetch all blocks from the channel. Returns flat list."""
    blocks = []
    page = 1
    ctx = ssl.create_default_context()

    while True:
        url = f"{API_URL}&page={page}"
        req = urllib.request.Request(url, headers={
            "Accept": "application/json",
            "User-Agent": "spatial-index-research/1.0"
        })
        try:
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                data = json.loads(resp.read().decode())
        except urllib.error.URLError as e:
            print(f"ERROR: are.na fetch failed: {e}", file=sys.stderr)
            sys.exit(2)

        contents = data.get("data") or data.get("contents") or []
        if not contents:
            break

        for b in contents:
            source = b.get("source") or {}
            attachment = b.get("attachment") or {}
            blocks.append({
                "id": b["id"],
                "type": b.get("type", b.get("class", "")),
                "title": b.get("title") or b.get("generated_title") or "",
                "url": source.get("url") or attachment.get("url") or "",
                "content": b.get("content") or "",
                "description": (b.get("description") or {}).get("markdown", "") or "",
                "added_at": b.get("connected_at") or b.get("created_at") or "",
            })

        page += 1
        if page > 5:
            break

    return blocks


def load_state() -> dict:
    path = os.path.abspath(STATE_FILE)
    if not os.path.exists(path):
        return {"last_seen_block_ids": []}
    with open(path) as f:
        return json.load(f)


def save_state(state: dict):
    with open(os.path.abspath(STATE_FILE), "w") as f:
        json.dump(state, f, indent=2)


def main():
    mark_seen = "--mark-seen" in sys.argv

    blocks = fetch_blocks()
    state = load_state()
    seen_ids = set(state.get("last_seen_block_ids", []))
    new_blocks = [b for b in blocks if b["id"] not in seen_ids]

    result = {
        "new_blocks": new_blocks,
        "total_blocks": len(blocks),
        "new_count": len(new_blocks),
    }

    if mark_seen and new_blocks:
        state["last_seen_block_ids"] = [b["id"] for b in blocks]
        state["block_count"] = len(blocks)
        state["last_updated"] = max((b.get("added_at", "") for b in blocks), default="")
        save_state(state)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
