from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Model for creating/updating items
class ItemModel(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    expiry_date: Optional[datetime] = None

# Model for filtering items
class ItemFilterModel(BaseModel):
    email: Optional[str] = None
    expiry_date: Optional[datetime] = None
    insert_date: Optional[datetime] = None
    quantity: Optional[int] = None
