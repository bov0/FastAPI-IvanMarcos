from typing import Optional
from pydantic import BaseModel

class Especie(BaseModel):
    id_especie: int
    nombre_especie: str
    descripcion: Optional[str]