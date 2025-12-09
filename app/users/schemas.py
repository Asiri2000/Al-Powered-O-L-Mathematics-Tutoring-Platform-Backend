# app/users/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime  # <--- Fix 1: Import datetime

# 1. Base Schema (Shared)
class UserBase(BaseModel):
    username: str
    grade: Optional[str] = None
    school: Optional[str] = None

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

class UserRoleUpdate(BaseModel):
    user_role: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    grade: Optional[str] = None
    school: Optional[str] = None

# 4. Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str | None = None