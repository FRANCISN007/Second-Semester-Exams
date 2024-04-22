from fastapi import APIRouter, HTTPException
#from Schemas.patient_schema import Patient, PatientCreateEdit
from Schemas.patient_schema import patients, PatientsCreateEdit
from services.patient_service import PatientService
#from services.doctor_service import DoctorService

patient_router = APIRouter()


@patient_router.get('/List', status_code=200)
def get_patients():
    data = PatientService.parse_patients(patient_data=patients)
    return {'message': 'successful', 'data': data}


@patient_router.get('/{patient_id}', status_code=200)
def get_doctor_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'successful', 'data': data} 

@patient_router.post('/', status_code=201)
def create_patient(payload: PatientsCreateEdit):
    data = PatientService.create_patient(payload)
    return {'message': 'Patient Profile Created', 'data': data}
    


@patient_router.put('/{patient_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: PatientsCreateEdit):
    data = PatientService.edit_patient(payload)
    return {'message': 'success', 'data': data}
      
      
          
@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'messge': 'user deleted successfully.'}