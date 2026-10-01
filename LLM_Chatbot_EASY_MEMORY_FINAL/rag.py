from vector_db import VectorDB

DB = VectorDB()


def retrieve(question, top_k=2):
    results = DB.search(question, top_k=top_k)
    context = "\n\n".join(item["text"] for item in results)
    sources = [item["source"] for item in results]
    return {"context": context, "sources": sources, "results": results}
