from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Model for creating/updating clock-in records
class ClockInModel(BaseModel):
    email: str
    location: Optional[str] = None
    clock_in_time: Optional[datetime] = None

# Model for filtering clock-in records
class ClockInFilterModel(BaseModel):
    email: Optional[str] = None
    location: Optional[str] = None
    insert_datetime: Optional[datetime] = None
