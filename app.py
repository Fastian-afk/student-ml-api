from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

APP_NAME = "student-ml-api"
VERSION_FILE = Path(__file__).parent / "VERSION"


def get_version() -> str:
    """Read the application version from the VERSION file."""
    return VERSION_FILE.read_text(encoding="utf-8").strip()


app = FastAPI(title=APP_NAME)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "version": get_version(),
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = request.value * 2

    return {
        "input": request.value,
        "prediction": prediction,
    }