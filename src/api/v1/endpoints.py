from typing import List, Dict, Any
from fastapi import status
from src.config import settings
from src.schema.employees import EmployeeResponse
from src.schema.metadata import RootResponse, InfoResponse

async def get_root() -> Dict[str,str]:
    return {
        "application": "Employee Management API",
        "status": "Running",
        "current_env":settings.ENV_NAME
    }

async def get_employees() -> List[Dict[str,str]]:
    return [{
        "employee_id": "1",
        "employee_name": "Gulshan",
        "department": "Platform Engineering"
    },{
        "employee_id": "2",
        "employee_name": "Gulshan1",
        "department": "Platform Engineering"
    }]

async def get_info() -> Dict[str,Any]:
    return {
        "env_name": settings.ENV_NAME,
        "p_t_d": {
            "team_name":settings.PLATFORM_TEAM,
            "contact_email":"@email.com"
        },
        "deployment_metadata":{
            "app_version": "1",
            "release_id": settings.DEPLOY_METADATA,
            "runtime_framework":"Fast API"
        }
    }

