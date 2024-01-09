from typing import Optional
from pydantic import BaseModel

class Habitat(BaseModel):
    id_habitat: int
    nombre_habitat: str
    descripcion: Optional[str]