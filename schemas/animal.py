from datetime import date
from typing import Optional
from pydantic import BaseModel

class Animal(BaseModel):
    id_animal: int
    nombre_animal: str
    fecha_nacimiento: Optional[date]
    edad: Optional[int]
    id_especie: int
    id_habitat: int