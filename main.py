from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import numpy as np, joblib
import models, crud, schemas
from database import engine, get_db
from fastapi import FastAPI, Depends, HTTPException
from schemas import PatientCreate, PredictionResponse

app = FastAPI(title="Health Prediction API")

# Create tables
models.Base.metadata.create_all(bind=engine)

# Load ML model and label encoder
model = joblib.load("health_model.pkl")
le = joblib.load("label_encoder.pkl")

# ---------------------------
# Endpoints
# ---------------------------

@app.post("/patients/", response_model=schemas.Patient)
def create_patient_endpoint(patient: PatientCreate, db: Session = Depends(get_db)):
    # Convert input to array for prediction
    features = np.array([[patient.age, patient.gender, patient.pressurhigh, patient.pressurlow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    status = le.inverse_transform([prediction])[0]
    return crud.create_patient(db=db, patient=patient, status=status)

@app.get("/patients/", response_model=list[schemas.Patient])
def get_patients_endpoint(db: Session = Depends(get_db)):
    return crud.get_patients(db)



@app.get("/patients/{id}", response_model=schemas.Patient)
def get_patient_endpoint(id: int, db: Session = Depends(get_db)):
    patient = crud.get_one(db, id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.post("/predict_risk/", response_model=PredictionResponse)
def predict_risk(patient: PatientCreate, db: Session = Depends(get_db)):
    features = np.array([[patient.age, patient.gender, patient.pressurhigh, patient.pressurlow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    risk_status = le.inverse_transform([prediction])[0]

    # Save patient with predicted status
    db_patient = crud.create_patient(db=db, patient=patient, status=risk_status)

    return {
        "prediction_code": int(prediction),
        "risk_status": risk_status,
        "message": f"Le modèle estime que le patient présente un {risk_status}"
    }

@app.put("/patients/{id}", response_model=schemas.Patient)
def update_patient_endpoint(id: int, patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    result = crud.update_patient(db, id, patient)
    return result
