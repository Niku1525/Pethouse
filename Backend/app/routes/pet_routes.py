from fastapi import APIRouter, UploadFile, File
from controllers.pet_controller import PetController
from models.pet_model import Pet
import shutil
import os

router = APIRouter(prefix="/pets", tags=["Pets"])
pet_controller = PetController()

if not os.path.exists("uploads"):
    os.makedirs("uploads")


@router.post("/create_pet")
async def create_pet(pet: Pet):
    return pet_controller.create_pet(pet)


@router.get("/get_pets")
async def get_pets():
    return pet_controller.get_pets()


@router.get("/get_pet/{pet_id}")
async def get_pet(pet_id: int):
    return pet_controller.get_pet(pet_id)


@router.delete("/delete_pet/{pet_id}")
async def delete_pet(pet_id: int):
    return pet_controller.delete_pet(pet_id)


# Subir imagen
@router.post("/upload_pet_image")
async def upload_pet_image(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"image_url": file_location}