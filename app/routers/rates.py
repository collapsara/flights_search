from datetime import datetime

import requests
import xmltodict

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core.crud import create_rate
from database import get_db


router = APIRouter()


@router.post("/rates")
async def get_rates(db: Session = Depends(get_db)):
    today = datetime.now()
    today_string = today.strftime("%d.%m.%Y")
    response = requests.get(f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={today_string}")
    result = xmltodict.parse(response.text, dict_constructor=dict)
    for item in result["rates"]["item"]:
        create_rate(db, item)
    return result["rates"]["item"]
