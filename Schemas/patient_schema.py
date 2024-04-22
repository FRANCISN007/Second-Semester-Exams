from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str

patients: dict[int, Patient] = {
    0: Patient(
        id=0, name='Frank', age="45", sex="M", weight="54kg", height="6.5m", phone="0901"
    ),
    1: Patient(
        id=1, name='Henry', age="25", sex="M", weight="78kg", height="5.4m", phone="0902"
    ),
    2: Patient(
        id=2, name='Mary', age="15", sex="F", weight="38kg", height="4.9m", phone="0903"
    )
}
  

#Patient= [
    #{"id": "1", "name": "frank", "age": "45", "sex":"m", "weight": "67kg", "height":"6.7m", "phone":"0801"},
    #{"id": "2", "name": "henry", "age": "20", "sex":"f", "weight": "85kg", "height":"7.7m", "phone":"0802"},
#]
    