# Easy LLM Chatbot — AI Systems Engineering

**Student:** MUHAMMAD ABUZAR  
**Matricola:** D03000198  
**Course:** AI Systems Engineering  
**Professor:** Prof. Roberto Pietrantuono

## What this project does

This is **one integrated chatbot**. It is intentionally written in simple Python so the implementation can be explained during the oral examination.

It demonstrates:

- Transformer / LLM inference with FLAN-T5-small
- Self-attention (`src_attention.py`)
- Self-supervised learning / MLM recipe (`training/train_mlm.py`)
- Transformer fine-tuning preparation (`training/train_sft.py`)
- Few-shot prompting
- Context engineering
- RAG
- Lightweight vector retrieval using TF-IDF + cosine similarity
- MCP-style structured tool/context interface
- A transparent agent router
- Preference/reward alignment demonstration
- Persistent conversation memory in `memory.json`
- CLI chatbot
- FastAPI API

The project does **not** expose or store private chain-of-thought. It uses concise explanations and an agent plan instead.

## 1. Install

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## 2. Run the chatbot

```bash
python chatbot.py
```

On the first run, Hugging Face downloads `google/flan-t5-small`. Internet is required for the first download unless the model is already cached.

Example:

```text
You: What is RAG?
Bot: RAG retrieves relevant documents and gives them to the language model before it answers.

You: My name is Abuzar.
Bot: Nice to meet you, Abuzar.

You: What is my name?
Bot: Your name is Abuzar.
```

The conversation is saved automatically in `memory.json`. The next time you start the program, recent saved conversation can be included in the prompt.

Commands:

- `exit` — close the chatbot
- `clear` — delete the saved conversation memory

## 3. How memory works

`memory.py` stores each question and generated answer as JSON. `context.py` adds recent turns to the next prompt.

This is simple persistent conversation memory, not model retraining. The chatbot does not change its neural-network weights when it remembers a conversation.

## 4. Run the API

```bash
uvicorn api:app --reload
```

Then open the local API documentation in your browser at:

```text
http://127.0.0.1:8000/docs
```

Use `POST /chat` with:

```json
{"question":"What is RAG?"}
```

`GET /memory` shows saved conversation history and `DELETE /memory` clears it.

## 5. Run tests

```bash
pytest -q
```

The tests cover the vector retrieval, RAG, MCP-style context, prompt/memory handling, and preference reward.

## 6. Project architecture

```text
User
  ↓
Context Engineering + Conversation Memory
  ↓
Agent
  ├── RAG → TF-IDF Vector Store → Local Knowledge Base
  └── MCP-style Knowledge Tool
  ↓
Few-Shot Prompt
  ↓
Transformer LLM (FLAN-T5-small)
  ↓
Answer
  ↓
Save Question + Answer to memory.json
```

Training concepts are kept separate:

```text
Pretrained Transformer
        ↓
Self-Supervised Learning / MLM
        ↓
Instruction Fine-Tuning
        ↓
Preference Alignment
        ↓
Deployment
```

## Important academic wording

- The MLM file is a training recipe and should only be described as completed training if it is actually executed and evaluated.
- `train_sft.py` is intentionally a simple preparation/demonstration file; do not claim that a fine-tuned model was produced unless training was actually run.
- `alignment.py` demonstrates preference scoring; it is **not** a claim of full RLHF or DPO training.
- `mcp.py` is an educational MCP-style interface, not a claim of complete production MCP protocol compliance.
- The vector store is lightweight TF-IDF retrieval, not a production-scale vector database.

## GitHub submission

Create a GitHub repository with a name such as:

`MUHAMMAD-ABUZAR-AI-SYSTEMS-ENGINEERING-LLM-CHATBOT`

Upload the **contents of this folder**, not only the ZIP file. The repository URL will look like:

`https://github.com/YOUR-GITHUB-USERNAME/MUHAMMAD-ABUZAR-AI-SYSTEMS-ENGINEERING-LLM-CHATBOT`

Put the final repository URL on the **first page of the PDF report**, as required by the professor's project instructions.

Do not upload passwords, API keys, or personal/private conversation data. `memory.json` is ignored by Git.
