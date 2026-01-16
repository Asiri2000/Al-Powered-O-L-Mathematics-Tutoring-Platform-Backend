from crewai import Task
from agents.quiz_agent import QuizAgent

def build_quiz_task(chapter, difficulty_level, weak_areas):
    return Task(
        description=f"""
Generate 5 O/L Mathematics MCQs.

Chapter: {chapter}
Difficulty: {difficulty_level}/5
Weak Areas: {weak_areas}

Rules:
- 4 options (A–D)
- One correct answer
- Short explanation
- O/L syllabus aligned
""",
        expected_output="""
[
  {
    "question": "...",
    "options": {"A":"", "B":"", "C":"", "D":""},
    "correct_answer": "A",
    "explanation": "...",
    "difficulty": 1
  }
]
""",
        agent=QuizAgent
    )
