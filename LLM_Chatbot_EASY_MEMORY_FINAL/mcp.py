def knowledge_context(question, retrieved):
    """Simple educational MCP-style tool/context interface."""
    return {
        "tool": "knowledge_context",
        "question": question,
        "context": retrieved["context"],
        "sources": retrieved["sources"],
    }
