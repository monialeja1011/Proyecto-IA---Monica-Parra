import pandas as pd

# ==========================================
# ANALISIS EXPLORATORIO DE DATOS
# Proyecto: Predicción de Producción Cafetera
# ==========================================

ARCHIVO = "data/produccion_cafetera_valle.csv"


def cargar_datos():
    """Carga el dataset agrícola del Valle del Cauca."""
    try:
        datos = pd.read_csv(
            ARCHIVO,
            sep=";",
            encoding="latin1"
        )
        return datos
    except FileNotFoundError:
        print("Error: no se encontró el archivo de datos.")
        return None


def mostrar_informacion(datos):
    """Muestra información general del dataset."""

    print("\n" + "=" * 60)
    print("ANÁLISIS DE PRODUCCIÓN CAFETERA")
    print("=" * 60)

    print("\nCantidad de registros:")
    print(len(datos))

    print("\nCantidad de columnas:")
    print(len(datos.columns))

    print("\nColumnas del dataset:")
    for columna in datos.columns:
        print(f"- {columna}")

    print("\nInformación general:")
    print(datos.info())

    print("\nPrimeros registros:")
    print(datos.head())


def analizar_cafe(datos):
    """Analiza únicamente los registros correspondientes al café."""

    cafe = datos[
        datos["Cultivo"]
        .astype(str)
        .str.contains("Caf", case=False, na=False)
    ].copy()

    print("\n" + "=" * 60)
    print("DATOS DE CAFÉ")
    print("=" * 60)

    print(f"\nTotal de registros de café: {len(cafe)}")

    print(f"Municipios con registros de café: {cafe['Municipio'].nunique()}")

    print("\nMunicipios:")
    municipios = sorted(cafe["Municipio"].dropna().unique())

    for municipio in municipios:
        print(f"- {municipio}")

    return cafe


def analizar_cartago(cafe):
    """Analiza los registros de café correspondientes a Cartago."""

    cartago = cafe[
        cafe["Municipio"]
        .astype(str)
        .str.contains("Cartago", case=False, na=False)
    ].copy()

    print("\n" + "=" * 60)
    print("CAFÉ EN CARTAGO")
    print("=" * 60)

    print(f"\nCantidad de registros: {len(cartago)}")

    if len(cartago) > 0:

        print("\nPeriodo disponible:")
        print(
            f"{cartago['Año'].min()} - "
            f"{cartago['Año'].max()}"
        )

        print("\nProducción histórica:")
        print(
            cartago[
                [
                    "Año",
                    "Hectareas_sembradas",
                    "Hectareas_cosechadas",
                    "Produccion_toneladas",
                    "Rendimiento_toneladas/hectareas"
                ]
            ].to_string(index=False)
        )

    return cartago


def revisar_datos_faltantes(cafe):
    """Revisa valores faltantes en los datos de café."""

    print("\n" + "=" * 60)
    print("DATOS FALTANTES")
    print("=" * 60)

    faltantes = cafe.isnull().sum()

    print(faltantes)


def convertir_columnas_numericas(cafe):
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


def main():

    datos = cargar_datos()

    if datos is None:
        return

    mostrar_informacion(datos)

    cafe = analizar_cafe(datos)

    cafe = convertir_columnas_numericas(cafe)

    revisar_datos_faltantes(cafe)

    analizar_cartago(cafe)


if __name__ == "__main__":
    main()
