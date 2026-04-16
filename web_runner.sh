#!/bin/sh
# Primero limpia los datos
python etl_proceso.py

# Luego enciende la página web
python servidor.py