from sqlalchemy import Column, Integer, String, Float
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    status = Column(String)
    glucose = Column(Float)
    pressurhigh = Column(Integer)
    pressurlow = Column(Integer)
    kcm = Column(Float)
    troponin = Column(Float)  
    impulse = Column(Integer)
    status = Column(String)

