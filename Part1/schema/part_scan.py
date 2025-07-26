from typing import Optional
from pydantic import BaseModel

class ScanEvent(BaseModel):
    part_id: str
    part_name: str
    timestamp: Optional[str] = None
    latitude: float
    longitude: float
    scanned_by: str
