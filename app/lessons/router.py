from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload # <--- Critical for relationships in Async
from typing import List

# Import your DB setup
from app.db.session import get_db 
from app.lessons.models import Lesson, LessonStep
from app.lessons.schemas import StepSchema, LessonSchema

router = APIRouter()

# 1. Get List of All Lessons
@router.get("/", response_model=List[LessonSchema])
async def get_all_lessons(db: AsyncSession = Depends(get_db)):
    # ASYNC QUERY:
    query = select(Lesson)
    result = await db.execute(query)
    lessons = result.scalars().all()
    return lessons

# 2. Get Full Content for ONE Lesson
@router.get("/{lesson_id}/content", response_model=List[StepSchema])
async def get_lesson_content(lesson_id: int, db: AsyncSession = Depends(get_db)):
    """
    Fetches the sequence of steps for a lesson, including answer options.
    """
    # A. Check if lesson exists
    query_lesson = select(Lesson).where(Lesson.id == lesson_id)
    result_lesson = await db.execute(query_lesson)
    lesson = result_lesson.scalar_one_or_none()
    
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    # B. Fetch Steps + Eager Load Options
    # In Async, we MUST use 'selectinload' to get the 'options' relationship 
    # immediately, otherwise it will crash when Pydantic tries to read it.
    query_steps = (
        select(LessonStep)
        .where(LessonStep.lesson_id == lesson_id)
        .order_by(LessonStep.order_index)
        .options(selectinload(LessonStep.options)) # <--- IMPORTANT: Pre-loads the answers
    )
    
    result_steps = await db.execute(query_steps)
    steps = result_steps.scalars().all()

    return steps