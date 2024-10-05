from fastapi import FastAPI
import uvicorn
from app.routers import pois, users, events

app = FastAPI()

app.include_router(pois.router, prefix="/pois", tags=["POIs"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])

if __name__ == "__main__":
    uvicorn.run("mian:app", host="127.0.0.1", port=8080, reload=True)