from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from tools.analytics_tool import get_diagnosis_data
from tools.rag_tool import rag_query
from services.remediation_service import generate_remediation

from crews.quiz_crew import build_quiz_crew
from crews.mock_exam_crew import build_mock_exam_crew
from services.learning_orchestrator import orchestrate_learning

from crews.tutor_feedback_crew import build_tutor_feedback_crew

app = FastAPI(title="Agentic AI Learning Service")

class LearnRequest(BaseModel):
    user_id: str
    chapter: str

class QuizRequest(BaseModel):
    chapter: str
    difficulty_level: int
    weak_areas: List[str]

class NextStepRequest(BaseModel):
    user_id: str
    chapter: str
    current_difficulty: Optional[int] = 3

class TutorFeedbackRequest(BaseModel):
    question: str
    selected_answer: str
    correct_answer: str

@app.post("/learn")
def learn(payload: LearnRequest):
    analytics = get_diagnosis_data(payload.user_id, payload.chapter)

    return {
        "mode": "LEARN",
        "analytics": analytics,
        "remediation": generate_remediation(payload.chapter, analytics),
        "rag": rag_query(f"Explain {payload.chapter} simply")
    }

@app.post("/generate-quiz")
def generate_quiz(payload: QuizRequest):
    crew = build_quiz_crew(
        payload.chapter,
        payload.difficulty_level,
        payload.weak_areas
    )
    return {"questions": crew.kickoff()}

@app.post("/generate-mock-exam")
def generate_mock_exam(payload: LearnRequest):
    crew = build_mock_exam_crew(payload.chapter)
    return {"exam": crew.kickoff()}

@app.post("/next-step")
def next_step(payload: NextStepRequest):
    analytics = get_diagnosis_data(payload.user_id, payload.chapter)
    return orchestrate_learning(analytics, payload.current_difficulty)

@app.post("/tutor-feedback")
def tutor_feedback(payload: TutorFeedbackRequest):
    crew = build_tutor_feedback_crew(
        payload.question,
        payload.selected_answer,
        payload.correct_answer
    )

    feedback = crew.kickoff()

    return {
        "mode": "TUTOR_FEEDBACK",
        "feedback": feedback
    }
