FROM python:3.10

# 1. Directorio de trabajo
WORKDIR /app

# 2. Copiar archivos (incluyendo tus .py y el .csv)
COPY . .

# 3. Instalar dependencias necesarias para el ETL y la Web
RUN pip install pandas flask

# 4. El comando "mágico" para Railway:
# Primero corre la limpieza (&& significa 'si sale bien, sigue')
# Luego corre el servidor (que se queda encendido y mantiene vivo el contenedor)
CMD ["sh", "-c", "python etl_proceso.py && python servidor.py"]