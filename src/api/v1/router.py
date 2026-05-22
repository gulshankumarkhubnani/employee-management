from fastapi import APIRouter
from typing import List
from src.schema.employees import EmployeeResponse
from src.schema.metadata import RootResponse, InfoResponse
from src.api.v1 import endpoints

v1_router = APIRouter()

v1_router.add_api_route("/",endpoints.get_root,response_model=RootResponse,methods=["GET"])
v1_router.add_api_route("/employee",endpoints.get_employees,response_model=List[EmployeeResponse],methods=["GET"])
v1_router.add_api_route("/info",endpoints.get_info,response_model=InfoResponse,methods=["GET"])