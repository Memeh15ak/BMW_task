from fastapi import FastAPI, Depends, HTTPException
from schema.part_scan import ScanEvent
from pymongo import MongoClient
from jose import JWTError, jwt
from datetime import datetime
import os

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client.bmw
collection = db.scans

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Dummy service center auth (JWT)
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("role") != "service_center":
            raise HTTPException(status_code=403)
    except JWTError:
        raise HTTPException(status_code=401)

@app.post("/scan-part")
def scan_part(data: ScanEvent):
    data_dict = data.dict()
    data_dict["timestamp"] = datetime.now().isoformat()
    collection.insert_one(data_dict)
    return {"message": "Scan saved."}

@app.get("/part/{part_id}")
def get_part_info(part_id: str, token: str = Depends(verify_token)):
    scans = list(collection.find({"part_id": part_id}, {"_id": 0}))
    return {"history": scans}
