# app/users/schemas.py
from pydantic import BaseModel, Field
from typing import Optional

# 1. Base Schema (Shared properties)
class UserBase(BaseModel):
    username: str
    grade: str
    school: str
    # Maps React's "studentName" to Python's "full_name"
    full_name: str = Field(..., alias="studentName") 

# 2. Schema for REGISTERING
class UserCreate(UserBase):
    password: str
    
    class Config:
        populate_by_name = True 

# 3. Schema for READING (Response)
class UserResponse(UserBase):
    id: int
    user_role: str      # <--- We send this back to the frontend
    is_active: bool
    created_at: str | None = None

    class Config:
        from_attributes = True

# 4. Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str | None = None