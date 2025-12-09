from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
# --- NEW IMPORTS ADDED HERE ---
from sqlalchemy import delete 
from sqlalchemy.exc import IntegrityError
from datetime import timedelta

# Import local modules
from app.db.session import get_db
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings
from app.users import models, schemas

router = APIRouter()

# --- 1. REGISTRATION ENDPOINT ---
@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    # 1. Check if username already exists
    result = await db.execute(select(models.User).filter(models.User.username == user_in.username))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already taken. Please choose another.",
        )

    # 2. Create new user object
    new_user = models.User(
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        grade=user_in.grade,
        school=user_in.school,
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


# --- 2. LOGIN ENDPOINT ---
@router.post("/login", response_model=schemas.Token)
async def login_access_token(
    db: AsyncSession = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    # 1. Find user by username
    result = await db.execute(select(models.User).filter(models.User.username == form_data.username))
    user = result.scalars().first()

    # 2. Check password
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Create Token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.id, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


# --- 3. GET CURRENT USER ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/users/login")

async def get_current_user(
    db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.User:
    from jose import jwt, JWTError
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    result = await db.execute(select(models.User).filter(models.User.id == int(user_id)))
    user = result.scalars().first()
    if user is None:
        raise credentials_exception
    return user

@router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


# --- 4. GET ALL USERS (For UserDetails Page) ---
@router.get("/", response_model=list[schemas.UserResponse])
async def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: AsyncSession = Depends(get_db)
):
    """Fetch all users to display in the table"""
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users


# --- 5. UPDATE USER ROLE ---
@router.put("/{user_id}/role", response_model=schemas.UserResponse)
async def update_user_role(
    user_id: int, 
    role_data: schemas.UserRoleUpdate, 
    db: AsyncSession = Depends(get_db)
):
    """Change user role (e.g., 'user' -> 'admin')"""
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    user.user_role = role_data.user_role
    await db.commit()
    await db.refresh(user)
    return user


# --- 6. UPDATE USER PROFILE ---
@router.put("/{user_id}", response_model=schemas.UserResponse)
async def update_user_profile(
    user_id: int,
    user_data: schemas.UserUpdate, # Make sure UserUpdate is in your schemas.py or remove this route if unused
    db: AsyncSession = Depends(get_db)
):
    """Update user profile (full_name, grade, school)"""
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_data.full_name is not None:
        user.full_name = user_data.full_name
    if user_data.grade is not None:
        user.grade = user_data.grade
    if user_data.school is not None:
        user.school = user_data.school
    
    await db.commit()
    await db.refresh(user)
    return user


# --- 7. DELETE USER (Fixed with Imports) ---
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db)
):
    """
    Hard delete a user using SQL. 
    Handles Foreign Key errors (e.g., if user has marks/results).
    """
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        # Perform Hard SQL Delete
        stmt = delete(models.User).where(models.User.id == user_id)
        await db.execute(stmt)
        await db.commit()
        
    except IntegrityError:
        await db.rollback()
        print(f"ERROR: Could not delete user {user_id} because they have linked data.")
        raise HTTPException(
            status_code=400, 
            detail="Cannot delete this user because they have associated data (marks, logs, etc.)."
        )
        
    return None