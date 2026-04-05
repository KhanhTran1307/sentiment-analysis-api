
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment Analysis API", version="1.0")

sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "name": "Sentiment Analysis API",
        "description": "Phan tich cam xuc van ban (Positive/Negative/Neutral)",
        "model": "cardiffnlp/twitter-roberta-base-sentiment-latest",
        "endpoints": ["/", "/health", "/predict"]
    }

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True}

@app.post("/predict")
def predict(data: TextInput):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text khong duoc de trong")
    try:
        result = sentiment_model(data.text)[0]
        return {
            "text": data.text,
            "label": result["label"],
            "score": round(result["score"], 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
