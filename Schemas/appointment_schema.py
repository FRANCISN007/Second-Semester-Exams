from pydantic import BaseModel
from datetime import date
from Schemas.doctor_schema import doctors, Doctor
from Schemas.patient_schema import patients, Patient


class Appointments(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    date: date
    
appointment: list[Appointments] = [
    Appointments(
        id=0, patient=patients[0], doctor=doctors[0], date='2024-01-25')
    
] 

