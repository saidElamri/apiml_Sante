from sqlalchemy import Column, Integer, String, Float
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    pressurhigh = Column(Float, nullable=False)
    pressurlow = Column(Float, nullable=False)
    glucose = Column(Float, nullable=False)
    kcm = Column(Float, nullable=False)
    troponin = Column(Float, nullable=False)
    impluse = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
