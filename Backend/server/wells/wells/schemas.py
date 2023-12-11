from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated, Dict
from datetime import datetime
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]

schema_descrption = {"example": {
                'sigla': 'Abreviatura de pozo',
                'area' : 'Area en la cual se encuentra el pozo',
                'cod_area' : 'Codigo de area en la cual se encuentra el pozo',
                'empresa' : 'Empresa a la cual pertence el pozo',
                'yacimiento' : 'Yacimiento a la cual pertence el pozo',
                'cod_yacimiento' : 'Codigo de yacimiento a la cual pertence el pozo' ,
                'formacion' : 'Formacion del pozos',
                'cuenca' : 'Cuenca a la cual pertenece el pozo',
                'provincia' : 'Provincia a la cual pertenece el pozo',
                'profundidad' : 'Prodfundidad del pozo' ,
                'tipopozo' : 'Tipo del pozo',
                'tipoextraccion' : 'Tipo de extraccion del pozo',
                'tipoestado' : 'Tipo de estado del pozo',
                'fecha_inicio_perf' : 'Fecha de inicio de perforacion del pozo',
                'fecha_fin_perf' : 'Fecha de finalizacion de perforacion del pozo',
                'fecha_inicio_prod' : 'Fecha de inicio de produccion del pozo',
                'fecha_fin_prod' : 'Fecha de finalizacion de produccion del pozo',
                'geojson' : 'Localizacion geografica del pozo'}}


class Wells(BaseModel):
    id: PyObjectId = Field(alias='_id', default=None)
    sigla: str
    area : str
    cod_area : Optional[str] = None
    empresa : str
    yacimiento : str
    cod_yacimiento : str
    formacion : Optional[str] = None
    cuenca : str
    provincia : str
    profundidad : int
    tipopozo : Optional[str] = None
    tipoextraccion : Optional[str] = None
    tipoestado : Optional[str] = None
    fecha_inicio_perf : Optional[datetime] = None
    fecha_fin_perf : Optional[datetime] = None
    fecha_inicio_prod : Optional[datetime] = None
    fecha_fin_prod : Optional[datetime] = None
    geojson : Dict[str, float] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=schema_descrption
    )

class WellsUpdate(BaseModel):
    sigla: Optional[str] = None
    area : Optional[str] = None
    cod_area : Optional[str] = None
    empresa : Optional[str] = None
    yacimiento : Optional[str] = None
    cod_yacimiento : Optional[str] = None 
    formacion : Optional[str] = None
    cuenca : Optional[str] = None
    provincia : Optional[str] = None
    profundidad : Optional[int] = None 
    tipopozo : Optional[str] = None
    tipoextraccion : Optional[str] = None
    tipoestado : Optional[str] = None
    fecha_inicio_perf : Optional[datetime] = None
    fecha_fin_perf : Optional[datetime] = None
    fecha_inicio_prod : Optional[datetime] = None
    fecha_fin_prod : Optional[datetime] = None
    geojson : Dict[str, float] = None
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra=schema_descrption,
    )

