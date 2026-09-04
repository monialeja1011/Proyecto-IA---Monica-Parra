import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# -------------------------------------------------
# FUNCIÓN PROPIA
# -------------------------------------------------
def calcular_estadisticas(producciones):
    producciones = np.array(producciones)

    estadisticas = {
        "media": np.mean(producciones),
        "maximo": np.max(producciones),
        "minimo": np.min(producciones),
        "desviacion": np.std(producciones)
    }

    return estadisticas


# -------------------------------------------------
# CARGAR DATOS
# -------------------------------------------------
archivo = "data/cafe_valle_limpio.csv"

try:
    datos = pd.read_csv(archivo, sep=";", encoding="utf-8")
except UnicodeDecodeError:
    datos = pd.read_csv(archivo, sep=";", encoding="latin1")


print("=" * 60)
print("ANÁLISIS EXPLORATORIO - PRODUCCIÓN DE CAFÉ")
print("=" * 60)


# -------------------------------------------------
# INFORMACIÓN GENERAL
# -------------------------------------------------
print("\nCantidad total de registros:", len(datos))
print("Cantidad de columnas:", len(datos.columns))

print("\nColumnas:")
print(list(datos.columns))


# -------------------------------------------------
# FILTRAR CAFÉ
# -------------------------------------------------
cafe = datos[
    datos["Cultivo"].astype(str).str.contains(
        "Caf", case=False, na=False
    )
].copy()

print("\nRegistros de café:", len(cafe))


# -------------------------------------------------
# FILTRAR CARTAGO
# -------------------------------------------------
cartago = cafe[
    cafe["Municipio"].astype(str).str.strip() == "Cartago"
].copy()

print("Registros de café en Cartago:", len(cartago))


# -------------------------------------------------
# CONVERTIR DATOS NUMÉRICOS
# -------------------------------------------------
columnas_numericas = [
    "Año",
    "Hectareas_sembradas",
    "Hectareas_cosechadas",
    "Produccion_toneladas",
    "Rendimiento_toneladas/hectareas"
]

for columna in columnas_numericas:
    cartago[columna] = pd.to_numeric(
        cartago[columna],
        errors="coerce"
    )


# -------------------------------------------------
# LISTA DE DICCIONARIOS
# -------------------------------------------------
lista_diccionarios = cartago.to_dict(orient="records")

print("\nLISTA DE DICCIONARIOS")
print("Cantidad:", len(lista_diccionarios))

print("\nPrimeros 2 registros:")
for registro in lista_diccionarios[:2]:
    print(registro)


# -------------------------------------------------
# NUMPY
# -------------------------------------------------
produccion = cartago["Produccion_toneladas"].dropna().values

estadisticas = calcular_estadisticas(produccion)


print("\nESTADÍSTICAS CON NUMPY")
print("-" * 40)

print(f"Producción promedio: {estadisticas['media']:.2f} toneladas")
print(f"Producción máxima: {estadisticas['maximo']:.2f} toneladas")
print(f"Producción mínima: {estadisticas['minimo']:.2f} toneladas")
print(f"Desviación estándar: {estadisticas['desviacion']:.2f} toneladas")


# -------------------------------------------------
# ENCONTRAR AÑOS DE MÁXIMO Y MÍNIMO
# -------------------------------------------------
fila_maxima = cartago.loc[
    cartago["Produccion_toneladas"].idxmax()
]

fila_minima = cartago.loc[
    cartago["Produccion_toneladas"].idxmin()
]

print("\nHALLAZGOS")
print("-" * 40)

print(
    f"1. La mayor producción registrada fue en "
    f"{int(fila_maxima['Año'])}, con "
    f"{fila_maxima['Produccion_toneladas']:.2f} toneladas."
)

print(
    f"2. La menor producción registrada fue en "
    f"{int(fila_minima['Año'])}, con "
    f"{fila_minima['Produccion_toneladas']:.2f} toneladas."
)


# -------------------------------------------------
# GRÁFICO
# -------------------------------------------------
cartago = cartago.sort_values("Año")

plt.figure(figsize=(10, 6))

plt.plot(
    cartago["Año"],
    cartago["Produccion_toneladas"],
    marker="o",
    label="Producción de café"
)

plt.title("Producción de Café en Cartago, Valle del Cauca")
plt.xlabel("Año")
plt.ylabel("Producción (toneladas)")
plt.grid(True)
plt.legend()

plt.tight_layout()

os.makedirs("data", exist_ok=True)

plt.savefig(
    "data/eda_cartago_produccion.png",
    dpi=150
)

plt.close()

print("\nGráfico guardado en:")
print("data/eda_cartago_produccion.png")

print("\nANÁLISIS TERMINADO")
