from fastapi import FastAPI
from routes.animal import animal
from config.openapi import tags_metadata

app = FastAPI(
    title="API de animales",
    description="Practica de 'aplicaciones en entorno Servidor' usando REST API con python and mysql",
    version="1.0",
    openapi_tags=tags_metadata,
)

app.include_router(animal)