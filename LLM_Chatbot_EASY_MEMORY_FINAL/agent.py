from rag import retrieve
from mcp import knowledge_context


def run_agent(question):
    """Simple transparent agent: retrieve when useful, otherwise answer directly."""
    retrieved = retrieve(question)

    if retrieved["sources"]:
        tool_result = knowledge_context(question, retrieved)
        return {
            "plan": "Use RAG + MCP context",
            "context": tool_result["context"],
            "sources": tool_result["sources"],
        }

    return {
        "plan": "Answer directly; no relevant local document found",
        "context": "",
        "sources": [],
    }
