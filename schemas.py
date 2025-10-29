from pydantic import BaseModel, Field, conint, confloat

# ------------------- User -------------------
class UserCreate(BaseModel):
    username: str
    password: str

# ------------------- Patient -------------------
class PatientCreate(BaseModel):
    age: conint(ge=0, le=120)
    gender: conint(ge=0)  # numeric for ML
    pressurhigh: confloat(ge=0)
    pressurlow: confloat(ge=0)
    glucose: confloat(ge=0)
    kcm: confloat(ge=0)
    troponin: confloat(ge=0)
    impluse: conint(ge=0)

class Patient(PatientCreate):
    id: int
    status: str

    class Config:
        from_attributes = True  # FastAPI v2 uses this instead of orm_mode

# ------------------- Prediction -------------------
class PredictionResponse(BaseModel):
    prediction_code: int
    risk_status: str
    message: str
