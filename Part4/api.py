from fastapi import FastAPI
from pydantic import BaseModel
from estimator import estimate_repair

app = FastAPI()

class RepairInput(BaseModel):
    parts: list
    region: str
    markup_percent: float = 10.0

@app.post("/estimate")
def get_estimate(data: RepairInput):
    return estimate_repair(data.parts, data.region, data.markup_percent)
