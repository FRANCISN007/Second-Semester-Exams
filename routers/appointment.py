from fastapi import APIRouter


appointment_router = APIRouter()

@appointment_router.get("/")
def read_root():
    return {"Book your Appointment"}



