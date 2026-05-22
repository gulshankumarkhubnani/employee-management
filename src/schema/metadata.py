from pydantic import BaseModel

class RootResponse(BaseModel):
    application:str
    status:str
    current_env:str

class PlatFormTeamDetails(BaseModel):
    team_name:str
    contact_email:str

class DeploymentMetaData(BaseModel):
    app_version: str
    release_id: str
    runtime_framework: str

class InfoResponse(BaseModel):
    env_name:str
    p_t_d:  PlatFormTeamDetails
    deployment_metadata:DeploymentMetaData
