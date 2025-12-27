from fastapi import APIRouter, UploadFile, File
router = APIRouter(prefix="/convert")
@router.post("")
async def convert(file: UploadFile = File(...)):
    return {"detail":"not implemented"}