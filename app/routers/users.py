from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import crud
from app.schemas import UserOut

router = APIRouter()

@router.get("/nearby")
async def get_nearby_users(lat: float, lon: float, radius: float, db: AsyncSession = Depends(get_db)):
    users = await crud.get_nearby_users(db, lat, lon, radius)
    
    return [{"id": user[0], "username": user[1], "location": user[2]} for user in users]
