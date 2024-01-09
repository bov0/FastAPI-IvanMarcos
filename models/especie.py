from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

especies = Table(
    "especies",
    meta,
    Column("id_especie", Integer, primary_key=True),
    Column("nombre_especie", String(255), nullable=False),
    Column("descripcion", String(255)),
)

meta.create_all(bind=engine, tables=[especies])
