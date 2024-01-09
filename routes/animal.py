from fastapi import APIRouter, HTTPException  
from config.db import conn
from models.animal import animales
from models.especie import especies
from models.habitat import habitats
from schemas.animal import Animal
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet

animal = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)

@animal.get(
    "/animales",
    tags=["animales"],
    response_model=List[Animal],
    description="Lista de todos los animales",
)
def get_animales():
    return conn.execute(animales.select()).fetchall()

@animal.get("/animales/{id}", tags=["animales"], response_model=Animal, description="Ver animal por ID único")
def get_animal(id: str):
    animal_resultado = conn.execute(animales.select().where(animales.c.id_animal == id)).first()
    
    if animal_resultado is None:
        raise HTTPException(status_code=404, detail="No se encontró ningún animal con el ID proporcionado")
    
    return animal_resultado


@animal.post("/", tags=["animales"], response_model=Animal, description="Crear un nuevo animal")
async def create_animal(animal_data: Animal):

    especie_resultado = conn.execute(especies.select().where(especies.c.id_especie == animal_data.id_especie)).first()
    habitat_resultado = conn.execute(habitats.select().where(habitats.c.id_habitat == animal_data.id_habitat)).first()

    if not animal_data.nombre_animal.isalpha():
        raise HTTPException(status_code=400, detail='El nombre del animal solo puede contener letras a-zA-Z')
    elif animal_data.edad < 0:
        raise HTTPException(status_code=400, detail='La edad no puede ser negativa')
    elif especie_resultado is None:
        raise HTTPException(status_code=404, detail="No existe ninguna especie con el ID proporcionado")
    elif habitat_resultado is None :
        raise HTTPException(status_code=404, detail="No existe ningun habitat con el ID proporcionado")
    else:
        new_animal = {
            "nombre_animal": animal_data.nombre_animal,
            "fecha_nacimiento": animal_data.fecha_nacimiento,
            "edad": animal_data.edad,
            "id_especie": animal_data.id_especie,
            "id_habitat": animal_data.id_habitat
        }

    result = conn.execute(animales.insert().values(new_animal))
    new_animal["id_animal"] = result.lastrowid
    return new_animal

@animal.put(
    "/animales/{id}", tags=["animales"], response_model=Animal, description="Modificar animal por ID"
)
def update_animal(animal_data: Animal, id: int):

    especie_resultado = conn.execute(especies.select().where(especies.c.id_especie == animal_data.id_especie)).first()
    habitat_resultado = conn.execute(habitats.select().where(habitats.c.id_habitat == animal_data.id_habitat)).first()
    
    if not animal_data.nombre_animal.isalpha():
        raise HTTPException(status_code=400, detail='El nombre del animal solo puede contener letras a-zA-Z')
    elif animal_data.edad < 0:
        raise HTTPException(status_code=400, detail='La edad no puede ser negativa')
    elif especie_resultado is None:
        raise HTTPException(status_code=404, detail="No existe ninguna especie con el ID proporcionado")
    elif habitat_resultado is None :
        raise HTTPException(status_code=404, detail="No existe ningun habitat con el ID proporcionado")
    else:
        conn.execute(
            animales.update()
            .values(
                nombre_animal=animal_data.nombre_animal,
                fecha_nacimiento=animal_data.fecha_nacimiento,
                edad=animal_data.edad,
                id_especie=animal_data.id_especie,
                id_habitat=animal_data.id_habitat
            )
            .where(animales.c.id_animal == id)
        )
        return conn.execute(animales.select().where(animales.c.id_animal == id)).first()

@animal.delete("/{id}", tags=["animales"], status_code=HTTP_204_NO_CONTENT)
def delete_animal(id: int):
    conn.execute(animales.delete().where(animales.c.id_animal == id))
    return conn.execute(animales.select().where(animales.c.id_animal == id)).first()
