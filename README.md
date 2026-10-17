
# Taller de Python y MySQL

## Objetivo
Crear una tabla de personas en MySQL y generar
100.000 registros ficticios.

## Tecnologias
- Python
- MySQL
- SQLAlchemy
- Faker
- DBeaver

## Instalacion
Instalar las bibliotecas con:

pip install -r requirements.txt

## Configuracion
Configurar la conexion a MySQL en el archivo .env.

## Ejecucion
Ejecutar el programa con:

python main.py

## Verificacion
Consultar los registros en DBeaver con:

SELECT COUNT(*) FROM personas_juanpablo;

## Estructura del proyecto

- `main.py`: genera e inserta los registros.
- `requirements.txt`: contiene las dependencias.
- `.env.example`: muestra la configuración necesaria.
- `.gitignore`: excluye archivos privados y temporales.

## Tecnologías utilizadas

- Python 3.10 o superior
- MySQL
- SQLAlchemy
- Faker
- PyMySQL
- python-dotenv

## Base de datos

La tabla utilizada es `personas_juanpablo` y contiene
100.000 registros ficticios generados por lotes de 5.000.