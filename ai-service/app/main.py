from fastapi import FastAPI
from pydantic import BaseModel

POSITIVE_WORDS = {
    "love", "amazing", "best", "fantastic", "wonderful", "great", "good", "happy", "like", "nice"
}
NEGATIVE_WORDS = {
    "hate", "terrible", "bad", "worst", "awful", "horrible", "stupid","disappointing", "sad", "angry", "poor"
}

class SentimentRequest(BaseModel):
    text: str

app = FastAPI(title="AI Sentiment Service (Rule-based Fallback)")

@app.get("/health")
def health():
    return {"status": "ok"}

def score_text(text: str) -> float:
    t = (text or "").lower()
    pos = sum(1 for w in POSITIVE_WORDS if w in t)
    neg = sum(1 for w in NEGATIVE_WORDS if w in t)
    total = pos + neg
    if total == 0:
        return 0.5  # neutral
    # simple bounded score between 0 and 1 skewed toward positive ratio
    return max(0.0, min(1.0, (pos + 1) / (total + 2)))

@app.post("/api/sentiment")
def sentiment(req: SentimentRequest):
    s = score_text(req.text)
    label = int(s >= 0.5)
    return {"label": label, "score": float(s)}
