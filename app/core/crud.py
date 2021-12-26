from sqlalchemy.orm import Session

from core import models, schemas


def create_rate(db: Session, rate: schemas.RateCreate):
    db_item = models.Rate(**rate)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_rate_value_by_currency_name(db: Session, currency_name: str):
    return db.query(models.Rate).filter(models.Rate.title == currency_name).first()

def get_rates(db: Session):
    return db.query(models.Rate).all()