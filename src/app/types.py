import datetime
from pydantic import BaseModel, Field


class GitHubSyncConfig(BaseModel):
    access_token: str = Field(..., description="GitHub personal access token.")
    repository: str = Field(..., description="Repository in the format 'owner-name/repo-name.")
    start_date: datetime.datetime = Field(..., description="The date to start looking for records at.")
    request_timeout: int = 300
