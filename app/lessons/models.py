from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    theme_slug = Column(String(50), nullable=False) # e.g., 'jungle', 'space'

    # Relationship to steps
    steps = relationship("LessonStep", back_populates="lesson", cascade="all, delete-orphan")


class LessonStep(Base):
    __tablename__ = "lesson_steps"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"))
    order_index = Column(Integer, nullable=False)
    
    # --- Split Screen Content ---
    # We use these instead of 'content_text' so we can show both theory and question
    theory_text = Column(Text, nullable=True)
    theory_media_url = Column(String(500), nullable=True)
    question_text = Column(Text, nullable=True)

    # Relationships
    lesson = relationship("Lesson", back_populates="steps")
    options = relationship("AnswerOption", back_populates="step", cascade="all, delete-orphan")


class AnswerOption(Base):
    __tablename__ = "answer_options"

    id = Column(Integer, primary_key=True, index=True)
    lesson_step_id = Column(Integer, ForeignKey("lesson_steps.id", ondelete="CASCADE"))
    option_text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False)

    # Relationships
    step = relationship("LessonStep", back_populates="options")