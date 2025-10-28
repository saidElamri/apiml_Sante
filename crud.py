from sqlalchemy.orm import Session
import models, schemas

def create_patient(db: Session, patient: schemas.PatientCreate, status: str):
    db_patient = models.Patient(**patient.dict(), status=status)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()
