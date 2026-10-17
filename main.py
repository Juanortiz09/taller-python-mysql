
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from faker import Faker

# Cargar la configuracion de conexion
load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

if not DATABASE_URL:
    raise ValueError("No se encontro DB_URL en el archivo .env")

# Conectar con MySQL
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


# Crear la clase base
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


# Crear la tabla en MySQL
Base.metadata.create_all(engine)

# Preparar la sesion y los datos ficticios
Session = sessionmaker(bind=engine)
fake = Faker("es_CO")

TOTAL = 100_000
LOTE = 5_000

# Generar e insertar los registros por lotes
with Session() as session:
    for inicio in range(0, TOTAL, LOTE):
        personas = []

        for i in range(inicio, min(inicio + LOTE, TOTAL)):
            persona = Persona(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                correo=f"persona{i}@example.com",
                telefono=fake.numerify(text="3#########"),
                ciudad=fake.city(),
                direccion=fake.address().replace("\n", " "),
                trabajo=fake.job(),
            )
            personas.append(persona)

        session.add_all(personas)
        session.commit()

        insertados = min(inicio + LOTE, TOTAL)
        print(f"Insertados {insertados} de {TOTAL}")

print("Proceso terminado. Se generaron 100.000 personas.")
