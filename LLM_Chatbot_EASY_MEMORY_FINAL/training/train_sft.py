import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Educational fine-tuning recipe. Full training requires a compatible Trainer setup.
MODEL = "google/flan-t5-small"
DATA = BASE_DIR / "data" / "instructions.jsonl"

with open(DATA, encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]

print(f"Loaded {len(rows)} instruction examples.")
print(f"Base model: {MODEL}")
print("This file is a simple, readable SFT preparation recipe.")

# The chatbot itself uses the pretrained FLAN-T5 model by default.
# A trained model should only be claimed after actually running and evaluating training.
AutoTokenizer.from_pretrained(MODEL)
AutoModelForSeq2SeqLM.from_pretrained(MODEL)
print("Model and tokenizer loaded successfully.")
