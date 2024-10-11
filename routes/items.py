from fastapi import APIRouter, HTTPException
from db.database import items_collection
from models.items import ItemModel, ItemFilterModel
from bson import ObjectId

from datetime import datetime

router = APIRouter()

# Helper function to convert MongoDB ObjectId to string
def item_helper(item) -> dict:
    item["_id"] = str(item["_id"])
    return item

# Create a new item
@router.post("/items")
async def create_item(item: ItemModel):
    item_dict = item.dict()
    item_dict['insert_date'] = datetime.utcnow()
    new_item = await items_collection.insert_one(item_dict)
    created_item = await items_collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

## Retrieve an item by ID
@router.get("/items/{id}")
async def get_item(id: str):
    # Validate if the ID is a valid ObjectId
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    # Try to fetch the item from the collection using ObjectId
    try:
        item = await items_collection.find_one({"_id": ObjectId(id)})
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching the item")

    if item:
        return item_helper(item)

    raise HTTPException(status_code=404, detail="Item not found")

# Filter items by various criteria
@router.post("/items/filter")
async def filter_items(filter: ItemFilterModel):
    query = {k: v for k, v in filter.dict().items() if v is not None}
    items = await items_collection.find(query).to_list(100)
    return [item_helper(item) for item in items]

# Delete an item by ID
@router.delete("/items/{id}")
async def delete_item(id: str):
    result = await items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item by ID
@router.put("/items/{id}")
async def update_item(id: str, item: ItemModel):
    update_data = {k: v for k, v in item.dict().items() if v is not None}
    updated_item = await items_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}
    )
    if updated_item.modified_count == 1:
        return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")
