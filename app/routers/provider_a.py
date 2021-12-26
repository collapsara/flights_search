import json
import time

from fastapi import APIRouter


router = APIRouter()


@router.post("/search")
async def search():
    with open('./static/response_a.json') as file:
        time.sleep(30)
        return json.loads(file.read())
    