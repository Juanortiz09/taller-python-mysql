
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

## Verificación de los datos

Para comprobar que los registros se guardaron correctamente en MySQL, ejecutar estas consultas:

```sql
USE personas_juanpablo;

SELECT COUNT(*) FROM personas_juanpablo;
```

El resultado esperado es de 100000 registros.

Para visualizar los primeros 10 registros:

```sql
SELECT * FROM personas_juanpablo LIMIT 10;
```


## Instalación y ejecución

1. Instalar Python 3.10 o superior.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

4. Configurar la variable `DB_URL` en el archivo `.env` con los datos de conexión a MySQL.
5. Ejecutar el programa:

```bash
python main.py
```

El programa crea la tabla si no existe y genera los registros por lotes de 5000.
