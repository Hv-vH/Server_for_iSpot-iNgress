from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func
from app.models import User, Event, POI

async def get_nearby_users(db: AsyncSession, lat: float, lon: float, radius: float):
    point = f"SRID=4326;POINT({lon} {lat})"
    query = select(User).filter(func.ST_DWithin(User.location, point, radius))
    result = await db.execute(query)
    return result.scalars().all()

async def get_nearby_events(db: AsyncSession, lat: float, lon: float, radius: float):
    point = f"SRID=4326;POINT({lon} {lat})"
    query = select(Event).filter(func.ST_DWithin(Event.location, point, radius))
    result = await db.execute(query)
    return result.scalars().all()