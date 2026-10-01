from pathlib import Path

from vector_db import VectorDB
from rag import retrieve
from mcp import knowledge_context
from context import build_prompt
from alignment import compare
from memory import clear_memory, save_turn, recent_memory


def test_vector_search():
    db = VectorDB()
    results = db.search("What is a Transformer?", top_k=2)
    assert results


def test_rag():
    result = retrieve("What is RAG?")
    assert result["sources"]
    assert result["context"]


def test_mcp():
    data = knowledge_context("test", {"context": "hello", "sources": ["x.txt"]})
    assert data["tool"] == "knowledge_context"


def test_prompt_and_memory():
    clear_memory()
    save_turn("My name is Abuzar", "Nice to meet you, Abuzar.")
    prompt = build_prompt("What is my name?")
    assert "My name is Abuzar" in prompt
    clear_memory()


def test_alignment():
    result = compare("A useful answer with enough detail.", "I don't know")
    assert result["chosen_reward"] >= result["rejected_reward"]
