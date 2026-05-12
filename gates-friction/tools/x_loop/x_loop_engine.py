#!/usr/bin/env python3
"""
The X-Loop Engine does not execute power.
It makes the next safe movement visible.

De X-loop voert geen macht uit.
De X-loop maakt de volgende veilige beweging zichtbaar.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys


# The script lives in tools/x_loop. Runtime outputs stay beside it so the
# movement remains local, inspectable and reversible.
BASE_DIR = Path(__file__).resolve().parent
NEXT_PROMPT_PATH = BASE_DIR / "NEXT_X_PROMPT.md"
LOG_PATH = BASE_DIR / "logs" / "x_movement_log.jsonl"


RED_TERMS = (
    "auto-commit",
    "auto commit",
    "auto-push",
    "auto push",
    "yolo",
    "force push",
    "delete all",
    "rm -rf",
)

YELLOW_TERMS = (
    "commit",
    "push",
    "ROI",
    "diagnosis",
    "audit",
    "therapy",
    "medical",
    "guarantee",
    "consultancy",
    "implementation",
    "solution",
)


def read_pasted_input() -> str:
    """Read direct paste input until a line containing only END."""
    print("Paste raw input, AI output or idea. Type END on its own line to finish.")

    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            # EOF is treated as a normal end of paste.
            break

        if line.strip() == "END":
            break

        lines.append(line)

    return "\n".join(lines).strip()


def detect_target_paths(raw_input: str) -> list[str]:
    """Find likely file paths without checking or editing the filesystem."""
    # This V1 pattern looks for slash-based repo paths such as docs/a.md or
    # tools/x_loop/x_loop_engine.py. It avoids URLs by skipping http prefixes.
    path_pattern = re.compile(
        r"(?<!https:)(?<!http:)(?<![\w.-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)"
    )

    paths: list[str] = []
    seen: set[str] = set()
    for match in path_pattern.finditer(raw_input):
        candidate = match.group(1).strip("`'\".,:;)")
        if candidate and candidate not in seen:
            seen.add(candidate)
            paths.append(candidate)

    return paths


def classify_input(raw_input: str, target_paths: list[str]) -> tuple[str, list[str]]:
    """Classify movement using transparent V1 rules."""
    risks: list[str] = []
    lowered = raw_input.lower()

    for term in RED_TERMS:
        if term.lower() in lowered:
            risks.append(f"RED term detected: {term}")

    if risks:
        return "RED", risks

    for term in YELLOW_TERMS:
        if term.lower() in lowered:
            risks.append(f"YELLOW term detected: {term}")

    if len(target_paths) > 3:
        risks.append(f"More than 3 target paths detected: {len(target_paths)}")

    if not target_paths:
        risks.append("No likely target file/path detected")

    if risks:
        return "YELLOW", risks

    return "GREEN", ["No RED or YELLOW V1 rule triggered"]


def summarize_raw_input(raw_input: str) -> str:
    """Create a short readable summary without interpreting truth."""
    compact = " ".join(raw_input.split())
    if len(compact) <= 240:
        return compact
    return compact[:237].rstrip() + "..."


def build_next_prompt(
    raw_input: str,
    target_paths: list[str],
    movement_signal: str,
    risks: list[str],
    timestamp: str,
) -> str:
    """Build the next safe Cursor/X prompt as a markdown artifact."""
    targets = "\n".join(f"- {path}" for path in target_paths) or "- No target path detected"
    risk_lines = "\n".join(f"- {risk}" for risk in risks)
    summary = summarize_raw_input(raw_input)

    return f"""# Next X Prompt

Generated timestamp: {timestamp}

Movement signal: {movement_signal}

The movement signal is a routing signal, not truth.

## Detected Risks

{risk_lines}

## Raw Input Summary

{summary}

## Detected Target Paths

{targets}

## Safe Cursor/X Prompt Template

Role:
You are the X execution layer inside the AsymX mechanism.

Repository:
Work in the current repository.

Movement signal:
{movement_signal}

Task:
Review the raw input summary and target paths. Make only the next safe, visible movement.

Target files:
{targets}

Hard rules:
- Do not commit.
- Do not push.
- Do not edit unrelated files.
- Do not add sources unless explicitly requested.
- Show git status --short.
- Show staged diff for target files.
- Then stop and wait.

Reminder:
The X-loop does not execute power. It makes the next safe movement visible.
"""


def append_log(
    raw_input: str,
    target_paths: list[str],
    movement_signal: str,
    risks: list[str],
    timestamp: str,
) -> None:
    """Append one JSONL movement entry."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": timestamp,
        "movement_signal": movement_signal,
        "detected_risks": risks,
        "target_paths": target_paths,
        "raw_input_summary": summarize_raw_input(raw_input),
        "note": "Movement signal is a routing signal, not truth.",
    }

    with LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> int:
    """Run the local X-loop prompt generator."""
    try:
        raw_input = read_pasted_input()
        if not raw_input:
            print("No input received. No files written.")
            return 0

        timestamp = datetime.now(timezone.utc).isoformat()
        target_paths = detect_target_paths(raw_input)
        movement_signal, risks = classify_input(raw_input, target_paths)
        next_prompt = build_next_prompt(
            raw_input=raw_input,
            target_paths=target_paths,
            movement_signal=movement_signal,
            risks=risks,
            timestamp=timestamp,
        )

        BASE_DIR.mkdir(parents=True, exist_ok=True)
        NEXT_PROMPT_PATH.write_text(next_prompt, encoding="utf-8")
        append_log(raw_input, target_paths, movement_signal, risks, timestamp)

        print(f"Movement signal: {movement_signal}")
        print("Detected risks:")
        for risk in risks:
            print(f"- {risk}")
        print(f"Next prompt: {NEXT_PROMPT_PATH}")
        print(f"Movement log: {LOG_PATH}")
        return 0
    except Exception as error:  # Keeps normal pasted text failures readable.
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
