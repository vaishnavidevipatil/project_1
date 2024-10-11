from fastapi import FastAPI

from routes import items, clock_in

app = FastAPI()

# Include the routers
app.include_router(items.router)
app.include_router(clock_in.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MongoDB Application!"}
