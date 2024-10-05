from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    location: str

class UserOut(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class EventBase(BaseModel):
    event_name: str
    location: str
    start_time: datetime

class EventOut(EventBase):
    id: int
    
    class Config:
        orm_mode = True

class POIBase(BaseModel):
    poi_name: str
    location: str