from typing import List, Optional

from pydantic import BaseModel


class RateBase(BaseModel):
    fullname: str
    title: str
    description: str
    quant: str
    index: str
    change: str

class RateCreate(RateBase):
    pass


class Rate(RateBase):
    id: int

    class Config:
        orm_mode = True
