import requests
from fastapi import APIRouter

router = APIRouter()

@router.get("/nearby")
async def get_nearby_users(lat: float, lon: float, radius: float):
    map_key = "035ceefa7dcb75f41b13c82b87b23dd5"
    url = f"https://restapi.amap.com/v3/place/around?key={map_key}&location={lon},{lat}&radius={radius}"
    response = requests.get(url)
    return response.json()