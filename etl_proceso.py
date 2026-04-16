import pandas as pd
import re

# =========================
# 1. EXTRACCIÓN (Extract)
# =========================
# Cargar archivo CSV (datos sucios)
df = pd.read_csv("datos_sucios.csv")

print("=== DATOS ORIGINALES ===")
print(df)


# =========================
# 2. LIMPIEZA (Transform)
# =========================

# ---- NOMBRES ----
# Si está vacío o null → reemplazar
df['nombre'] = df['nombre'].fillna('Desconocido')
df['nombre'] = df['nombre'].replace('', 'Desconocido')


# ---- EDAD ----
# Convertir a número (si falla → NaN)
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')

# Rellenar con media
df['edad'] = df['edad'].fillna(df['edad'].mean())


# ---- CORREO ----
def correo_valido(correo):
    if pd.isna(correo):
        return False
    return re.match(r"[^@]+@[^@]+\.[^@]+", correo)

# Si no cumple formato → marcar
df['correo'] = df['correo'].apply(lambda x: x if correo_valido(x) else 'correo_invalido')


# ---- SALARIO ----
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

# Usar mediana (mejor para datos reales)
df['salario'] = df['salario'].fillna(df['salario'].median())


# ---- FECHAS ----
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')

# Rellenar con fecha actual
df['fecha_registro'] = df['fecha_registro'].fillna(pd.Timestamp.today())


print("\n=== DATOS LIMPIOS ===")
print(df)


# =========================
# 3. CARGA (Load)
# =========================
df.to_csv("datos_limpios.csv", index=False)

print("\nArchivo generado: datos_limpios.csv")