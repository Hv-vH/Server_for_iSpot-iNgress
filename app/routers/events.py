from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("/nearby")
async def get_nearby_users(lat: float, lon: float, radius: float, db: AsyncSession = Depends(get_db)):
    events = await crud.get_nearby_events(db, lat, lon, radius)
    return [{"id": event[0], "event_name": event[1], "location": event[2], "start_time": event[3]} for event in events]
