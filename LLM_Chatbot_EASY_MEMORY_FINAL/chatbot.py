import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from agent import run_agent
from context import build_prompt
from memory import save_turn, clear_memory

MODEL = os.getenv("CHATBOT_MODEL", "google/flan-t5-small")

print(f"Loading model: {MODEL}")
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)


def ask(question):
    result = run_agent(question)
    prompt = build_prompt(question, result["context"])

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )

    output = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=False,
    )

    answer = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    save_turn(question, answer)

    return {
        "answer": answer,
        "agent_plan": result["plan"],
        "sources": result["sources"],
    }


if __name__ == "__main__":
    print("\nLLM Chatbot started.")
    print("Type 'exit' to stop or 'clear' to delete saved conversation memory.\n")

    while True:
        question = input("You: ").strip()

        if not question:
            continue
        if question.lower() == "exit":
            print("Goodbye!")
            break
        if question.lower() == "clear":
            clear_memory()
            print("Bot: Conversation memory cleared.")
            continue

        try:
            result = ask(question)
            print("Bot:", result["answer"])
            print("Agent:", result["agent_plan"])
            if result["sources"]:
                print("Sources:", ", ".join(result["sources"]))
            print()
        except Exception as error:
            print("Bot: The model could not answer.")
            print("Error:", error)
            print()
