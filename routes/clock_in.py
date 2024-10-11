from fastapi import APIRouter, HTTPException
from db.database import clock_in_collection
from models.clock_in import ClockInModel, ClockInFilterModel
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# Helper function to convert MongoDB ObjectId to string
def clock_in_helper(record) -> dict:
    record["_id"] = str(record["_id"])
    return record

# Create a new clock-in record
@router.post("/clock-in")
async def create_clock_in(clock_in: ClockInModel):
    clock_in_dict = clock_in.dict()
    clock_in_dict['insert_datetime'] = datetime.utcnow()  # Automatically set the insert date-time
    new_record = await clock_in_collection.insert_one(clock_in_dict)
    created_record = await clock_in_collection.find_one({"_id": new_record.inserted_id})
    return clock_in_helper(created_record)

# Retrieve a clock-in record by ID
@router.get("/clock-in/{id}")
async def get_clock_in(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    record = await clock_in_collection.find_one({"_id": ObjectId(id)})
    if record:
        return clock_in_helper(record)
    raise HTTPException(status_code=404, detail="Record not found")

# Filter clock-in records
@router.post("/clock-in/filter")
async def filter_clock_in_records(filter: ClockInFilterModel):
    query = {k: v for k, v in filter.dict().items() if v is not None}
    records = await clock_in_collection.find(query).to_list(100)
    return [clock_in_helper(record) for record in records]

# Delete a clock-in record by ID
@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Clock-in record deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

# Update a clock-in record by ID (excluding insert_datetime)
@router.put("/clock-in/{id}")
async def update_clock_in(id: str, clock_in: ClockInModel):
    update_data = {k: v for k, v in clock_in.dict().items() if v is not None}
    updated_record = await clock_in_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}
    )
    if updated_record.modified_count == 1:
        return {"message": "Clock-in record updated"}
    raise HTTPException(status_code=404, detail="Record not found")
