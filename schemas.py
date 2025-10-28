from pydantic import BaseModel, Field, conint, confloat, constr

# Schéma pour POST /patients (création)

class PatientCreate(BaseModel):
    age: conint(ge=0, le=120) = Field(..., description="Âge du patient entre 0 et 120")

    gender: constr(min_length=1, max_length=10) = Field(..., description="Genre du patient")

    status: constr(min_length=1, max_length=50) = Field(..., description="Statut du patient")

    pressurhigh: confloat(ge=0) = Field(..., description="Tension artérielle systolique")
    pressurlow:confloat(ge=0) = Field(..., description="Tension artérielle systolique")
    glucose: confloat(ge=0) = Field(..., description="Taux de glucose")

    kcm: confloat(ge=0) = Field(..., description="Valeur KCM")

    troponin: confloat(ge=0) = Field(..., description="Taux de tropin")

    impluse: conint(ge=0) = Field(..., description="Fréquence cardiaque / impulsion")

# Schéma pour GET /patients (réponse avec id)
class Patient(PatientCreate):
    id: int
    status: str
class Config:
        orm_mode = True

class PredictionResponse(BaseModel):
    prediction_code: int
    risk_status: str
    message: str