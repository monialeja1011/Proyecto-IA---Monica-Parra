import pandas as pd

# ==========================================
# PREPARACIÓN DE DATOS PARA MACHINE LEARNING
# Proyecto: Predicción de Producción Cafetera
# ==========================================

ARCHIVO = "data/cafe_valle_limpio.csv"


def cargar_datos():
    """Carga el dataset limpio."""

    try:
        datos = pd.read_csv(
            ARCHIVO,
            sep=";",
            encoding="utf-8"
        )

        print("Dataset limpio cargado correctamente.")
        return datos

    except FileNotFoundError:
        print("Error: no se encontró el archivo limpio.")
        return None


def seleccionar_variables(datos):
    """Selecciona las variables que utilizará el modelo."""

    columnas = [
        "Año",
        "Hectareas_sembradas",
        "Hectareas_cosechadas",
        "Municipio",
        "Produccion_toneladas"
    ]

    datos_modelo = datos[columnas].copy()

    return datos_modelo


def convertir_municipios(datos):
    """Convierte el municipio en variables numéricas."""

    datos = pd.get_dummies(
        datos,
        columns=["Municipio"],
        dtype=int
    )

    return datos


def separar_variables(datos):
    """Separa las variables de entrada y la variable objetivo."""

    X = datos.drop(
        "Produccion_toneladas",
        axis=1
    )

    y = datos["Produccion_toneladas"]

    return X, y


def mostrar_resultados(X, y):
    """Muestra información de los datos preparados."""

    print("\n" + "=" * 60)
    print("DATOS PREPARADOS PARA MACHINE LEARNING")
    print("=" * 60)

    print("\nCantidad de registros:")
    print(len(X))

    print("\nCantidad de variables de entrada:")
    print(X.shape[1])

    print("\nVariables de entrada:")
    for columna in X.columns:
        print(f"- {columna}")

    print("\nVariable objetivo:")
    print("Produccion_toneladas")

    print("\nPrimeros registros de X:")
    print(X.head())

    print("\nPrimeros valores de y:")
    print(y.head())


def main():

    datos = cargar_datos()

    if datos is None:
        return

    datos_modelo = seleccionar_variables(datos)

    datos_modelo = convertir_municipios(datos_modelo)

    X, y = separar_variables(datos_modelo)

    mostrar_resultados(X, y)


if __name__ == "__main__":
    main()
