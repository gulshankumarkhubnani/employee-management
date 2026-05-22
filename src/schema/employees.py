from pydantic import BaseModel, Field

class EmployeeResponse(BaseModel):
    employee_id: str=Field(...,description="id",example=["1"])
    employee_name: str=Field(...,description="name",example=["gulshan"])
    department: str=Field(...,description="Department",example=["CDT"])