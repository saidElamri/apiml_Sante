from sqlalchemy.orm import Session
import models, schemas

def create_patient(db: Session, patient: schemas.PatientCreate, status: str):
    db_patient = models.Patient(**patient.model_dump(), status=status)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()

def get_one(db: Session,id: int):
    
    return db.query(models.Patient).filter(models.Patient.id == id).first()


def update_patient(db: Session, id: int, patient: schemas.PatientCreate):
    patient_db = db.query(models.Patient).filter(models.Patient.id == id).first()
    
    if not patient_db:
        return {"msg": "Patient not found"}
    
    # Update fields from the incoming patient object
    patient_db.age = patient.age
    patient_db.gender = patient.gender
    patient_db.pressurhigh = patient.pressurhigh
    patient_db.pressurlow = patient.pressurlow
    patient_db.kcm = patient.kcm
    patient_db.troponin = patient.troponin
    patient_db.impluse = patient.impluse
    patient_db.glucose = patient.glucose  # add this if you have it in your schema
    
    # Save changes
    db.commit()
    db.refresh(patient_db)
    
    return patient_db
