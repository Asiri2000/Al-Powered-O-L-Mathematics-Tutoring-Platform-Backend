from crewai import Crew
from tasks.quiz_task import build_quiz_task

def build_quiz_crew(chapter, difficulty_level, weak_areas):
    task = build_quiz_task(chapter, difficulty_level, weak_areas)
    return Crew(
        agents=[task.agent],
        tasks=[task],
        verbose=True
    )
