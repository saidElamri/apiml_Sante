from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_BCRYPT_LENGTH = 72  # bcrypt max password length

# ---------------- User ----------------
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    truncated_password = user.password[:MAX_BCRYPT_LENGTH]  # truncate to 72 chars
    hashed_password = pwd_context.hash(truncated_password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    truncated_password = plain_password[:MAX_BCRYPT_LENGTH]  # truncate before verifying
    return pwd_context.verify(truncated_password, hashed_password)

# ---------------- Patient ----------------
def create_patient(db: Session, patient: schemas.PatientCreate, status: str, owner_id: int):
    db_patient = models.Patient(**patient.dict(), status=status, owner_id=owner_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients_by_user(db: Session, user_id: int):
    return db.query(models.Patient).filter(models.Patient.owner_id == user_id).all()
