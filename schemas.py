from pydantic import BaseModel, Field, conint, confloat

# Input schema for creating a patient
class PatientCreate(BaseModel):
    age: conint(ge=0, le=120) = Field(..., description="Âge du patient entre 0 et 120")
    gender: conint(ge=0) = Field(..., description="Genre du patient encodé en nombre (0=Homme, 1=Femme, etc.)")
    pressurhigh: confloat(ge=0) = Field(..., description="Tension artérielle systolique (haute)")
    pressurlow: confloat(ge=0) = Field(..., description="Tension artérielle diastolique (basse)")
    glucose: confloat(ge=0) = Field(..., description="Taux de glucose dans le sang")
    kcm: confloat(ge=0) = Field(..., description="Valeur KCM")
    troponin: confloat(ge=0) = Field(..., description="Taux de troponine (biomarqueur cardiaque)")
    impluse: conint(ge=0) = Field(..., description="Fréquence cardiaque / impulsion")


# Schema for GET /patients responses
class Patient(PatientCreate):
    id: int
    status: str

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2


# Schema for /predict_risk response
class PredictionResponse(BaseModel):
    prediction_code: int
    risk_status: str
    message: str
