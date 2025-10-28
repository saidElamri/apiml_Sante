from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crude
from database import engine, SessionLocal
import joblib
import numpy as np

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Health Prediction API")

# Load model
model = joblib.load("health_model.pkl")
le = joblib.load("label_encoder.pkl")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    # Convert input to numpy array for prediction
    features = np.array([[patient.age, patient.gender, patient.pressurehight, patient.pressurelow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    status = le.inverse_transform([prediction])[0]

    return crude.create_patient(db=db, patient=patient, status=status)

@app.get("/patients/")
def get_patients(db: Session = Depends(get_db)):
    return crude.get_patients(db)
@app.post("/predict_risk/")
def predict_risk(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    # Convert input to numpy array for prediction
    features = np.array([[patient.age, patient.gender, patient. pressurhigh, patient.pressurlow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    risk_status = le.inverse_transform([prediction])[0]
    db_patient = crude.create_patient(db=db, patient=patient, status=risk_status)
    return {
        "prediction_code": int(prediction),
        "risk_status": risk_status,
        "message": f"Le modèle estime que le patient présente un {risk_status}"
    }
