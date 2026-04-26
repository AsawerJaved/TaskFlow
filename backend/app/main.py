from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing routers
from app.routes import tasks

# Initializing the FastAPI application
app = FastAPI()

# Including tasks routes
app.include_router(tasks.router)

# Adding CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)