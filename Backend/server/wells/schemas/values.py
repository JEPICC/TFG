from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated
from datetime import datetime
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]

schema_descrption = {"example": {
                'idmedidor' : 'Identificados de Medidor',
                'timestamp' : 'Valor temporal de valor',
                'value': 'Medicion en funcion de tiempo',
                'estado': 'Estado del Medidor'
                    }}

class Values(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)
    idmedidor : str
    timestamp : datetime
    value: float
    estado: bool

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=schema_descrption
    )

# class ValuesResponse(BaseModel):
#     idmedidor : Optional[str] = None
#     timestamp : Optional[datetime] = None
#     value: Optional[float] = None
#     estado: Optional[bool] = None
   
#     model_config = ConfigDict(
#         arbitrary_types_allowed=True,
#         json_encoders={ObjectId: str},
#         json_schema_extra=schema_descrption,
#     )

