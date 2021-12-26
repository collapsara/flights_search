from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float


from database import Base


class Rate(Base):

    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    title = Column(String)
    description = Column(Float)
    quant = Column(Integer)
    index = Column(String)
    change = Column(Float)
