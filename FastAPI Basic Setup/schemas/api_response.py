from pydantic import BaseModel
from typing import Union, Optional


class APIResponse(BaseModel):
    status_code: int = 200
    message: Optional[str] = ""
    data: Union[list, dict] = []
    success: bool = True

    class Config:
        from_attributes = True
