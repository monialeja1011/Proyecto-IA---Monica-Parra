import pandas as pd

# ==========================================
# LIMPIEZA DE DATOS
# Proyecto: Predicción de Producción Cafetera
# ==========================================

ARCHIVO_ORIGINAL = "data/produccion_cafetera_valle.csv"
ARCHIVO_LIMPIO = "data/cafe_valle_limpio.csv"


def cargar_datos():
    """Carga el archivo original de datos agrícolas."""

    try:
        datos = pd.read_csv(
            ARCHIVO_ORIGINAL,
            sep=";",
            encoding="latin1"
        )

        print("Archivo cargado correctamente.")
        return datos

    except FileNotFoundError:
        print("Error: no se encontró el archivo de datos.")
        return None


def filtrar_cafe(datos):
    """Selecciona únicamente los registros correspondientes al café."""

    cafe = datos[
        datos["Cultivo"]
        .astype(str)
        .str.contains("Caf", case=False, na=False)
    ].copy()

    print(f"Registros de café encontrados: {len(cafe)}")

    return cafe


def normalizar_municipios(cafe):
    """Normaliza nombres de municipios para evitar duplicados."""

    equivalencias = {
        "Andalucia": "Andalucía",
        "Bolivar": "Bolívar",
        "Guadalajara de Buga": "Buga",
        "Santiago de Cali": "Cali",
        "Calima": "Calima Darién",
        "El Aguila": "El Águila"
    }

    cafe["Municipio"] = cafe["Municipio"].replace(equivalencias)

    return cafe


def convertir_numeros(cafe):
    """Convierte las columnas numéricas al formato correcto."""

    columnas_numericas = [
        "Hectareas_sembradas",
        "Hectareas_cosechadas",
        "Produccion_toneladas",
        "Rendimiento_toneladas/hectareas"
    ]

    for columna in columnas_numericas:

        cafe[columna] = (
            cafe[columna]
            .astype(str)
            .str.replace(",", ".", regex=False)
        )

        cafe[columna] = pd.to_numeric(
            cafe[columna],
            errors="coerce"
        )

    return cafe


def revisar_datos(cafe):
    """Realiza una revisión final de los datos."""

    print("\n" + "=" * 60)
    print("REVISIÓN FINAL")
    print("=" * 60)

    print(f"\nCantidad de registros: {len(cafe)}")

    print(f"Cantidad de municipios: {cafe['Municipio'].nunique()}")

    print("\nValores faltantes:")

    faltantes = cafe.isnull().sum()

    print(faltantes)

    print("\nTipos de datos:")

    print(cafe.dtypes)


def guardar_datos(cafe):
    """Guarda el conjunto de datos limpio."""

    cafe.to_csv(
        ARCHIVO_LIMPIO,
        sep=";",
        index=False,
        encoding="utf-8"
    )

    print("\nArchivo limpio guardado en:")
    print(ARCHIVO_LIMPIO)


def main():

    datos = cargar_datos()

    if datos is None:
        return

    cafe = filtrar_cafe(datos)

    cafe = normalizar_municipios(cafe)

    cafe = convertir_numeros(cafe)

    revisar_datos(cafe)

    guardar_datos(cafe)


if __name__ == "__main__":
    main()
