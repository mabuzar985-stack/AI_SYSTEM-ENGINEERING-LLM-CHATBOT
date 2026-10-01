from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
KB_DIR = BASE_DIR / "knowledge_base"


def load_documents():
    documents = []
    for path in sorted(KB_DIR.glob("*.txt")):
        documents.append((path.name, path.read_text(encoding="utf-8")))
    return documents


class VectorDB:
    def __init__(self):
        self.documents = load_documents()
        self.texts = [text for _, text in self.documents]
        self.vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
        self.matrix = self.vectorizer.fit_transform(self.texts)

    def search(self, question, top_k=2, min_score=0.05):
        query = self.vectorizer.transform([question])
        scores = cosine_similarity(query, self.matrix)[0]
        ranked = scores.argsort()[::-1]

        results = []
        for index in ranked[:top_k]:
            score = float(scores[index])
            if score >= min_score:
                name, text = self.documents[index]
                results.append({"source": name, "text": text, "score": score})
        return results
