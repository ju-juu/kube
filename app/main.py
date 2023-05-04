from fastapi import FastAPI
from .routes.example import router as example_router

app = FastAPI()

# Include the example router
app.include_router(example_router, prefix="/example")