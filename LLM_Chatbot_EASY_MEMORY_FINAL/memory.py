import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path(__file__).resolve().parent / "memory.json"


def load_memory():
    if not MEMORY_FILE.exists():
        return []
    try:
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_turn(question, answer):
    memory = load_memory()
    memory.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "question": question,
        "answer": answer,
    })
    MEMORY_FILE.write_text(
        json.dumps(memory, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def recent_memory(limit=6):
    return load_memory()[-limit:]


def clear_memory():
    MEMORY_FILE.write_text("[]", encoding="utf-8")
