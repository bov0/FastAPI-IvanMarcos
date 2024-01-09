from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, BLOB
from config.db import meta, engine

habitats = Table(
    "habitats",
    meta,
    Column("id_habitat", Integer, primary_key=True),
    Column("nombre_habitat", String(255), nullable=False),
    Column("nombre_imagen", String(255), nullable=False),
    Column("imagen_habitat", BLOB),
)

meta.create_all(bind=engine, tables=[habitats])
