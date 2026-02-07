from typing import Optional, Literal

from pydantic import BaseModel, Field, model_validator
from langchain.output_parsers import PydanticOutputParser


class DocumentExtraction(BaseModel):
    document_type: Literal["kg5b", "vertrag", "sonstiges"]
    ...

parser = PydanticOutputParser(pydantic_object=DocumentExtraction)

try:
    valid_reponse = parser.parse(response)

except Exception as e:
