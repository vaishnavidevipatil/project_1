import uvicorn
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)