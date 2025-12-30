from pydantic import BaseModel
from typing import List, Optional

# 1. Option Schema (Smallest part)
class OptionSchema(BaseModel):
    id: int
    option_text: str
    is_correct: bool

    class Config:
        from_attributes = True # Allows Pydantic to read SQLAlchemy models

# 2. Step Schema (The Screen Data)
class StepSchema(BaseModel):
    id: int
    order_index: int
    theory_text: Optional[str] = None
    theory_media_url: Optional[str] = None
    question_text: Optional[str] = None
    
    # Nested list of options for this specific step
    options: List[OptionSchema] = []

    class Config:
        from_attributes = True

# 3. Lesson Schema (The Container)
class LessonSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    theme_slug: str
    
    class Config:
        from_attributes = True