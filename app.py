# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI API Running Successfully"}

@app.post("/predict")
def predict(data: dict):
    value = data.get("value", 0)

    if value > 50:
        result = "High"
    else:
        result = "Low"

    return {
        "prediction": result
    }