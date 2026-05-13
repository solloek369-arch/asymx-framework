from pathlib import Path
import re

ROOT = Path(".").resolve()

PATTERNS = {
    "CLAIM_GATE": [
        r"sligro",
        r"sap",
        r"as400",
        r"manco",
        r"short.?pick",
        r"internal",
        r"proof",
        r"roi",
    ],
    "VAULT_RISK": [
        r"vault",
        r"source",
        r"raw",
        r"archive",
        r"chat_recovery",
        r"private",
    ],
    "PROMPT_TRACE": [
        r"prompt",
        r"deepsearch",
        r"x_execution",
        r"gemini",
        r"grok",
        r"perplexity",
    ],
    "PERSONAL_RISK": [
        r"family",
        r"children",
        r"kinderen",
        r"gezondheid",
        r"health",
        r"persoonlijk",
    ],
}

SAFE_PUBLIC_ROOTS = {
    "README.md",
    "LICENSE",
    ".gitignore",
    "source",
    "looking-glass",
    "living-routes",
    "workbench",
    "gates-friction",
    "archive-vault",
}

IGNORE_DIRS = {".git", "__pycache__", ".DS_Store"}

def classify(path: Path):
    s = str(path).lower()
    hits = []

    for label, patterns in PATTERNS.items():
        for pat in patterns:
            if re.search(pat, s):
                hits.append(label)
                break

    if not hits:
        return "LEAF", "KEEP_VISIBLE"

    if "PERSONAL_RISK" in hits:
        return "THORN", "HUMAN_GATE_REQUIRED"

    if "VAULT_RISK" in hits and "CLAIM_GATE" in hits:
        return "THORN", "REVIEW_BEFORE_PUBLIC"

    if "VAULT_RISK" in hits:
        return "COMPOST", "CHECK_SOURCE_BOUNDARY"

    if "PROMPT_TRACE" in hits:
        return "SPORE", "LABEL_AS_TRACE"

    if "CLAIM_GATE" in hits:
        return "THORN", "CLAIM_GATE_REQUIRED"

    return "SPORE", "FOLLOW_SIGNAL"

def main():
    rows = []

    for path in ROOT.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.is_dir():
            continue

        rel = path.relative_to(ROOT)
        status, route = classify(rel)
        if status != "LEAF":
            rows.append((status, route, str(rel)))

    print("# Spore Engine Scan")
    print()
    print("| Status | Route | Path |")
    print("|---|---|---|")

    for status, route, rel in sorted(rows):
        print(f"| {status} | {route} | `{rel}` |")

if __name__ == "__main__":
    main()
