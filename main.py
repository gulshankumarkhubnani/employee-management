import uvicorn
from fastapi import FastAPI
from src.config import settings
from src.api.v1.router import v1_router
from src.api.system import system_router

app= FastAPI(title="Employee Management API", description="Production-grade versioned core API.",version="1.0.0")

app.include_router(system_router)
app.include_router(v1_router, prefix=settings.API_V1_STR)

if __name__=="__main__":
    uvicorn.run("main.py",host="0.0.0.0", port=8000, log_level="info")