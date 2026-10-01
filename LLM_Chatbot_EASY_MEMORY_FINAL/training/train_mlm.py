from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForMaskedLM,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

MODEL = "distilbert-base-uncased"
text = (BASE_DIR / "data" / "ssl_text.txt").read_text(encoding="utf-8").splitlines()
text = [x for x in text if x.strip()]

dataset = Dataset.from_dict({"text": text})
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForMaskedLM.from_pretrained(MODEL)


def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=64)

tokenized = dataset.map(tokenize, batched=True, remove_columns=["text"])
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

args = TrainingArguments(
    output_dir="mlm_model",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    logging_steps=1,
    report_to="none",
)

Trainer(model=model, args=args, train_dataset=tokenized, data_collator=collator).train()
model.save_pretrained("mlm_model")
tokenizer.save_pretrained("mlm_model")
print("Saved MLM model to mlm_model/")
