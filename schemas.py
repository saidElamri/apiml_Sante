from pydantic import BaseModel

class PatientBase(BaseModel):
    age: int
    gender: int
    pressurehigh: int   # ✅ fixed typo: 'pressurehight' → 'pressurehigh'
    pressurelow: int
    glucose: float
    kcm: float
    troponin: float
    impulse: int        # ✅ fixed typo: 'impluse' → 'impulse'

class PatientCreate(PatientBase):
    status: str         # ✅ include 'status' for creation if it's required

class Patient(PatientBase):
    id: int
    status: str

    class Config:
        from_attributes = True   # ✅ replaces orm_mode in Pydantic v2
