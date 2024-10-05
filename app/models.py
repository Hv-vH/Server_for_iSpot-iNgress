from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import Geography
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    location = Column(Geography(geometry_type='POINT', srid=4326))

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(100), index=True)
    location = Column(Geography(geometry_type='POINT', srid=4326))
    start_time = Column(TIMESTAMP)

class POI(Base):
    __tablename__ = "pois"

    id = Column(Integer, primary_key=True, index=True)
    poi_name = Column(String(100), index=True)
    location = Column(Geography(geometry_type='POINT', srid=4326))