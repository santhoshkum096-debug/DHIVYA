from pydantic import BaseModel, Field
from typing import Optional

class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2, max_length=80)
    party_one: str = Field(..., min_length=2, max_length=200)
    party_two: str = Field(..., min_length=2, max_length=200)
    effective_date: str = Field(..., min_length=2, max_length=50)
    jurisdiction: str = Field(..., min_length=2, max_length=200)
    terms: str = Field(..., min_length=5, max_length=10000)
    additional_details: Optional[str] = Field(default="", max_length=10000)

class ExportRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=50000)
