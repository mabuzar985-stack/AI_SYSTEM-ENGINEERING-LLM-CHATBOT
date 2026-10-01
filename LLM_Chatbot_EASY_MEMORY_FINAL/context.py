from memory import recent_memory

FEW_SHOT = [
    ("What is RAG?", "RAG retrieves relevant documents and gives them to the language model before it answers."),
    ("What is attention?", "Attention helps a Transformer decide which tokens are important for the current token."),
]


def build_prompt(question, retrieved_context="", memory=None):
    examples = "\n".join(f"Q: {q}\nA: {a}" for q, a in FEW_SHOT)
    memory = recent_memory() if memory is None else memory

    history = ""
    if memory:
        history = "\n".join(
            f"User: {item['question']}\nAssistant: {item['answer']}"
            for item in memory
        )
    else:
        history = "No previous conversation."

    context = retrieved_context or "No relevant local knowledge was found."

    return f"""You are a helpful AI Systems Engineering chatbot.
Give the most useful answer you can. Be clear, factual, and concise.
Use the retrieved context when it is relevant. Do not invent facts from the context.
Use conversation history only when it helps answer the current question.
Do not reveal private chain-of-thought; give a concise explanation instead.

Few-shot examples:
{examples}

Recent conversation history:
{history}

Retrieved knowledge:
{context}

Current user question:
{question}

Answer:
"""
