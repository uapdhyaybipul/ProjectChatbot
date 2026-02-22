from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel
from src.core.security import create_access_token
from src.core.dependencies import get_current_user
from src.app.schemas.auth_achema import AuthRequest

router = APIRouter()


@router.post("/login")
async def login(request: AuthRequest):
    if request.username != "admin" or request.password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    else:
        access_token = create_access_token(data={"sub": request.username})
        return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
