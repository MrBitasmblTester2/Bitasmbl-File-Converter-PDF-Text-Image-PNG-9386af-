from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import convert
app = FastAPI()
app.include_router(convert.router)
app.mount("/files", StaticFiles(directory="converted"), name="files")