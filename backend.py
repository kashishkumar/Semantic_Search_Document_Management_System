import os 
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, ServiceContext, load_index_from_storage
from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
import shutil 
from pathlib import Path

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return templates.TemplateResponse("home.html", {"request": "request"})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return None

@app.get("/query/{query}")
async def query(query: str):
    return None 

@app.get("/summarise/")
async def summarise(query: str):
    return None

def load_data():
    return None

def index_data():
    return None

def build_query_engine():
    return None

def output_response():
    return None

def summarize():
    return None



 












9820113342 - Poonam 