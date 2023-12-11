from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]

schema_descrption = {"example": {
                'id_antenna': 'Identificador de antena',
                'codigo_error': 'Numero Error',
                'descripcion': 'Descripcion error',
                'timestamp': 'Fecha evento'
}}

class AntennaStates(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)
    id_antenna: str
    codigo_error: int
    descripcion: str
    timestamp: datetime

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=schema_descrption
    )

class AntennaStatesResponse(BaseModel):
    id_antenna: Optional[str] = None
    codigo_error: Optional[int] = None
    descripcion: Optional[str] = None
    timestamp: Optional[datetime] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=schema_descrption
    )