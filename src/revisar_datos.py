import pandas as pd

ARCHIVO = "data/produccion_cafetera_valle.csv"

# Intentar cargar el archivo con diferentes codificaciones
try:
    datos = pd.read_csv(ARCHIVO, sep=";", encoding="utf-8")
except UnicodeDecodeError:
    datos = pd.read_csv(ARCHIVO, sep=";", encoding="latin1")

print("\nColumnas del dataset:")
print(datos.columns.tolist())

print("\nCantidad de registros:")
print(len(datos))

print("\nMunicipios disponibles que contienen 'Cartago':")
print(
    datos[
        datos["Municipio"]
        .astype(str)
        .str.contains("Cartago", case=False, na=False)
    ]["Municipio"].unique()
)

print("\nCultivos disponibles que contienen 'Caf':")
print(
    datos[
        datos["Cultivo"]
        .astype(str)
        .str.contains("Caf", case=False, na=False)
    ]["Cultivo"].unique()
)

print("\nRegistros de Café en Cartago:")
cartago_cafe = datos[
    datos["Municipio"].astype(str).str.contains("Cartago", case=False, na=False)
    & datos["Cultivo"].astype(str).str.contains("Caf", case=False, na=False)
]

print(cartago_cafe.to_string(index=False))

print("\nCantidad de registros de Café en Cartago:")
print(len(cartago_cafe))
