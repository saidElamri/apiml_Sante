# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
import numpy as np
import joblib
import jwt
from datetime import datetime, timedelta

import models, crud, schemas
from database import engine, SessionLocal, Base

# -------------------------------
# JWT Config
# -------------------------------
SECRET_KEY = "your_secret_key_here"  # change to something secure
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# -------------------------------
# FastAPI app
# -------------------------------
app = FastAPI(title="Health Prediction API")

# Create tables
Base.metadata.create_all(bind=engine)

# Load ML model and label encoder
model = joblib.load("health_model.pkl")
le = joblib.load("label_encoder.pkl")

# -------------------------------
# Dependencies
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = crud.get_user_by_username(db, username)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# -------------------------------
# User endpoints
# -------------------------------
@app.post("/signup", response_model=dict)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    crud.create_user(db, user)
    return {"msg": "User created successfully"}

@app.post("/login", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# -------------------------------
# Patient endpoints
# -------------------------------
@app.post("/patients/", response_model=schemas.Patient)
def create_patient_endpoint(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # protected route
):
    # Convert input to array for prediction
    features = np.array([[patient.age, patient.gender, patient.pressurhigh, patient.pressurlow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    status = le.inverse_transform([prediction])[0]
    return crud.create_patient(db=db, patient=patient, status=status, owner_id=current_user.id)

@app.get("/patients/", response_model=list[schemas.Patient])
def get_patients_endpoint(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # protected route
):
    return crud.get_patients_by_user(db, user_id=current_user.id)

# -------------------------------
# Risk prediction endpoint
# -------------------------------
@app.post("/predict_risk/", response_model=schemas.PredictionResponse)
def predict_risk(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # protected route
):
    features = np.array([[patient.age, patient.gender, patient.pressurhigh, patient.pressurlow,
                          patient.glucose, patient.kcm, patient.troponin, patient.impluse]])
    prediction = model.predict(features)[0]
    risk_status = le.inverse_transform([prediction])[0]

    # Save patient linked to user
    db_patient = crud.create_patient(db=db, patient=patient, status=risk_status, owner_id=current_user.id)

    return {
        "prediction_code": int(prediction),
        "risk_status": risk_status,
        "message": f"Le modèle estime que le patient présente un {risk_status}"
    }
