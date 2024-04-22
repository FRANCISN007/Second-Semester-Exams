from fastapi import HTTPException
from Schemas.doctor_schema import doctors, Doctor, DoctorsCreateEdit, doctors


class DoctorService:
   
   @staticmethod
   def parse_doctors(doctor_data):
        data = []
        for doct in doctor_data:
            data.append(doctors[doct])
        return data
   @staticmethod
   def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        return doctor
   #def get_doctor_by_id(self, doctors: list[Doctor], doctor_id: str):
   
      #for doctor in doctors:
         #if doctor.id == doctor_id:
           #return doctor
        
      #return None

   #doctor_service = DoctorService()

   @staticmethod
   def create_doctor(doctor_data: DoctorsCreateEdit):
        id = len(doctors)
        doctor = Doctor(
            id=id,
            **doctor_data.model_dump()
        )
        doctors[id] = doctor
        return doctor

   @staticmethod
   def edit_doctor(payload: DoctorsCreateEdit):
        id = len(doctors)
        doctor = Doctor(
            id=id,
            **payload.model_dump()
        )
        doctors[id] = doctor
        return doctor
   

   @staticmethod
   def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        del doctors[doctor_id]       





