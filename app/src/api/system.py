from fastapi import APIRouter, Response, status
from typing import Dict

system_router=APIRouter()

@system_router.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check(response: Response)-> Dict[str,str]:
    health_flag=True
    if not health_flag:
        response.status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status":"unhealthy"}
    return {"status":"healthy"}
