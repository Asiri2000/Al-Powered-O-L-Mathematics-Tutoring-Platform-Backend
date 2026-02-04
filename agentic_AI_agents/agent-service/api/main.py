from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from generators.registry import get_generator

print("✅ LOADED agent-service/api/main.py")

app = FastAPI(title="Agentic AI Learning Service")


class QuizRequest(BaseModel):
    grade: int
    topic: str
    difficulty_level: int
    weak_areas: List[str]


@app.post("/generate-quiz")
def generate_quiz(payload: QuizRequest):
    generator = get_generator(payload.grade, payload.topic)
    question = generator(payload.difficulty_level)

    return {
        "questions": [question]
    }
