import json

from sqlalchemy.orm import Session
from celery.result import AsyncResult
from fastapi import APIRouter, Depends


from app.celery_worker import flights_search
from app.core.crud import get_rate_value_by_currency_name
from app.helpers.currency import set_price_by_currency
from database import get_db


router = APIRouter()


@router.post("/search")
async def search():
    search_id = flights_search.delay().id
    return {
        "search_id": search_id
    }


@router.post("/search/{search_id}/{currency}")
async def search_by_id(search_id: str, currency: str, db: Session = Depends(get_db)):
    async_result = AsyncResult(search_id)
    status = async_result.state
    if status == "SUCCESS":
        result = async_result.get()
        result = set_price_by_currency(db, result, currency)
    else:
        result = None
    return {
        "search_id": search_id,
        "status": status,
        "items": result,
    }
