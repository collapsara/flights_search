import json

from sqlalchemy.orm import Session
from celery.result import AsyncResult
from fastapi import APIRouter, Depends


from app.celery_worker import flights_search
from app.core.crud import get_rate_value_by_currency_name
from database import get_db


router = APIRouter()


@router.post("/search")
def search():
    search_id = flights_search.delay().id
    return {
        "search_id": search_id
    }


@router.post("/search/{search_id}/{currency}")
def search_by_id(search_id: str, currency: str, db: Session = Depends(get_db)):
    status =  AsyncResult(search_id).state
    rate = get_rate_value_by_currency_name(db, 'USD')
    if status == "SUCCESS":
        result = AsyncResult(search_id).get()
    else:
        result = None
    return {
        "search_id": search_id,
        "status": status,
        "items": result,
        "current_rate": rate,
    }
