import os
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    ENV_NAME:str= os.getenv("ENVIRONMENT_NAME","DEV")
    PLATFORM_TEAM:str=os.getenv("P_T","P E C")
    DEPLOY_METADATA:str=os.getenv("D_M","v1")
    API_V1_STR:str="/v1"

settings=Setting()
