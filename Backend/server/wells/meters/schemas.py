from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated
from datetime import datetime
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]

schema_descrption = {"example": {
                'idpozo': 'Identificador de pozo',
                'tag' : 'Identificador de medidor',
                'tipo': 'press / temp / flow',
                'unidad_medida' : 'UOM',
                'marca' : 'Marca del equipo',
                'modelo' : 'Modelo del equipo',
                'proveedor' : 'Proveedor del equipo',
                'fecha_instalacion' : 'fecha de instalación'}}

class Meters(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)
    idpozo: str
    tag : str
    tipo: str
    unidad_medida : str
    marca : Optional[str] = None
    modelo : Optional[str] = None
    proveedor : Optional[str] = None
    fecha_instalacion : datetime

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=schema_descrption
    )
    

class MetersUpdate(BaseModel):
    idpozo: Optional[str] = None
    tag : Optional[str] = None
    tipo: Optional[str] = None
    unidad_medida : Optional[str] = None
    marca : Optional[str] = None
    modelo : Optional[str] = None
    proveedor : Optional[str] = None
    fecha_instalacion : Optional[datetime] = None
   
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra=schema_descrption,
    )

