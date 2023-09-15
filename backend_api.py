from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from pathlib import Path
from backend_functions import load_data, index_data, build_query_engine, output_response, show_response, summarize

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return templates.TemplateResponse("home.html", {"request": "request"})

documents = {}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_content = await file.read()  # Read file content
    doc_id = str(uuid4())  # Generate a unique ID for the document
    documents[doc_id] = file_content  # Store in memory
    return {
        "doc_id": doc_id,
        "filename": file.filename
    }


@app.get("/query/{query}")
async def query(query: str):
    return None


@app.get("/summarise/")
async def summarise(query: str):
    return None


