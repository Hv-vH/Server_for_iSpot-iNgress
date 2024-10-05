from fastapi import FastAPI
import uvicorn
import sys
import os

# 获取项目根目录的路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from app.routers import pois, users, events

app = FastAPI()

app.include_router(pois.router, prefix="/pois", tags=["POIs"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)