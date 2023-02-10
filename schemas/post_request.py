from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PostRequestPayload(BaseModel):
    """
    Represents a data structure to be validated when user interfaces with the API.
    """
    # Obligatory field to be passed in the Payload
    field_a: str = Field(..., min_length=1, max_length=48, example="A Field.")

    # Optional field, in this case a list of strings
    string_list: Optional[List[str]] = Field("", example="['A', 'B']")
    
    # Optional field that will be populated automatically with UTC standard (without offset)
    timestamp: Optional[str] = str(datetime.utcnow())