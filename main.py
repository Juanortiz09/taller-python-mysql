

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Integer, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from faker import Faker

# Cargar la configuración de conexión
load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró DB_URL en el archivo .env")

# Conectar con MySQL
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


class Base(DeclarativeBase):
    pass


# Definir la tabla de personas
class Persona(Base):
    __tablename__ = "personas_juanpablo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(150), unique=True)
    telefono: Mapped[str] = mapped_column(String(30))
    ciudad: Mapped[str] = mapped_column(String(100))
    direccion: Mapped[str] = mapped_column(String(200))
    trabajo: Mapped[str] = mapped_column(String(120))


# Crear la tabla si todavía no existe
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
fake = Faker("es_CO")

TOTAL = 100_000
LOTE = 5_000

with Session() as session:
    # Consultar cuántos registros existen
    existentes = session.scalar(
        select(func.count()).select_from(Persona)
    )

    if existentes >= TOTAL:
        print(f"La tabla ya tiene {existentes} personas. No se insertaron más registros.")
    else:
        faltantes = TOTAL - existentes
        print(f"Hay {existentes} personas. Se generarán {faltantes} más.")

        siguiente = session.scalar(
            select(func.max(Persona.id))
        ) or 0

        generados = 0

        while generados < faltantes:
            cantidad = min(LOTE, faltantes - generados)
            personas = []

            for _ in range(cantidad):
                siguiente += 1
                persona = Persona(
                    nombre=fake.first_name(),
                    apellido=fake.last_name(),
                    correo=f"persona_{siguiente}@example.com",
                    telefono=fake.numerify(text="3#########"),
                    ciudad=fake.city(),
                    direccion=fake.address().replace("\n", " "),
                    trabajo=fake.job(),
                )
                personas.append(persona)

            session.add_all(personas)
            session.commit()

            generados += cantidad
            print(f"Insertados {generados} de {faltantes} nuevos registros.")

print("Proceso terminado.")
