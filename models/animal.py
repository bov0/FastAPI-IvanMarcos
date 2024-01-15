from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, BLOB
from config.db import meta, engine

animales = Table(
    "animales",
    meta,
    Column("id_animal", Integer, primary_key=True),
    Column("nombre_animal", String(255), nullable=False),
    Column("fecha_nacimiento", Date),
    Column("edad", Integer),
    Column("id_especie", Integer, ForeignKey('especies.id_especie'), nullable=False),
    Column("imagen", BLOB),
    Column("id_habitat", Integer, ForeignKey('habitats.id_habitat'), nullable=False),
)

meta.create_all(bind=engine,tables=[animales])
