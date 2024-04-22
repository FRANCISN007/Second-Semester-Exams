from pydantic import BaseModel
from typing import Union

class Doctor(BaseModel):
    id: int
    name: str
    specialization:str
    phone: str
    is_available: Union[bool, None] = None

class DoctorsCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: Union[bool, None] = None
      
    
doctors: dict[int, Doctor] = {
    0: Doctor(
        id=0, name='Dr Ogbe', specialization="Gynecology", phone='0901'
    ),
    1: Doctor(
        id=1, name='Dr Eze', specialization="Dermatology", phone='0902'
    ),
    2: Doctor(
        id=2, name='Dr Francis', specialization="General Surgery", phone='0902'
    )
}
