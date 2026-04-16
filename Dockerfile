FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install pandas
#para que siga corriendo 
CMD ["sh", "-c", "python etl_proceso.py && tail -f /dev/null"]