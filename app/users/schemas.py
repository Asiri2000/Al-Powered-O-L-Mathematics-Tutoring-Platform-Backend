# app/users/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime  # <--- Fix 1: Import datetime

# 1. Base Schema (Shared)
class UserBase(BaseModel):
    username: str
    grade: str
    school: str

# 2. Schema for REGISTERING (Input)
class UserCreate(UserBase):
    password: str
    # Input alias: Frontend sends "studentName", we map it to "full_name"
    full_name: str = Field(..., alias="studentName")

    # This allows us to use the field name 'full_name' if needed
    model_config = ConfigDict(populate_by_name=True)

# 3. Schema for READING (Response)
class UserResponse(UserBase):
    id: int
    user_role: str
    is_active: bool
    
    # Fix 2: Change type from str to datetime so Pydantic can read the DB object
    created_at: Optional[datetime] = None 
    
    # Fix 3: Handle the name mapping explicitly for Output
    # We use serialization_alias to send "studentName" to Frontend
    # We use validation_alias to read "full_name" from Database
    full_name: str = Field(..., validation_alias="full_name", serialization_alias="studentName")

    model_config = ConfigDict(from_attributes=True)

# 4. Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str | None = None