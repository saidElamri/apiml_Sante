from pydantic import BaseModel, Field, conint, confloat

# Input schema for creating a patient
class PatientCreate(BaseModel):
    age: conint(ge=0, le=120) = Field(..., description="Âge du patient entre 0 et 120")
    gender: conint(ge=0) = Field(..., description="Genre du patient encodé en nombre")  # numeric for ML
    pressurhigh: confloat(ge=0) = Field(..., description="Tension artérielle systolique")
    pressurlow: confloat(ge=0) = Field(..., description="Tension artérielle diastolique")
    glucose: confloat(ge=0) = Field(..., description="Taux de glucose")
    kcm: confloat(ge=0) = Field(..., description="Valeur KCM")
    troponin: confloat(ge=0) = Field(..., description="Taux de troponine")
    impluse: conint(ge=0) = Field(..., description="Fréquence cardiaque / impulsion")

# Schema for GET /patients responses
class Patient(PatientCreate):
    id: int
    status: str

    class Config:
        orm_mode = True

# Schema for /predict_risk response
class PredictionResponse(BaseModel):
    prediction_code: int
    risk_status: str
    message: str
