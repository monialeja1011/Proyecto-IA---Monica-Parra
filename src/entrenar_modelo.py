import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


ARCHIVO = "data/cafe_valle_limpio.csv"
ARCHIVO_MODELO = "data/modelo_cafetero.pkl"


def cargar_datos():
    """Carga el dataset limpio."""

    try:
        datos = pd.read_csv(
            ARCHIVO,
            sep=";",
            encoding="utf-8"
        )

        print("Dataset cargado correctamente.")
        return datos

    except FileNotFoundError:
        print("Error: no se encontró el dataset.")
        return None


def preparar_datos(datos):
    """Prepara las variables para el modelo."""

    columnas = [
        "Año",
        "Hectareas_sembradas",
        "Hectareas_cosechadas",
        "Municipio",
        "Produccion_toneladas"
    ]

    datos = datos[columnas].copy()

    datos = pd.get_dummies(
        datos,
        columns=["Municipio"],
        dtype=int
    )

    return datos


def dividir_datos(datos):
    """Divide los datos por años."""

    entrenamiento = datos[datos["Año"] <= 2021].copy()
    prueba = datos[datos["Año"] >= 2022].copy()

    X_entrenamiento = entrenamiento.drop(
        "Produccion_toneladas",
        axis=1
    )

    y_entrenamiento = entrenamiento["Produccion_toneladas"]

    X_prueba = prueba.drop(
        "Produccion_toneladas",
        axis=1
    )

    y_prueba = prueba["Produccion_toneladas"]

    return (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba
    )


def entrenar_modelo(X_entrenamiento, y_entrenamiento):
    """Entrena el modelo Random Forest."""

    modelo = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    modelo.fit(
        X_entrenamiento,
        y_entrenamiento
    )

    return modelo


def evaluar_modelo(modelo, X_prueba, y_prueba):
    """Evalúa el modelo."""

    predicciones = modelo.predict(X_prueba)

    mae = mean_absolute_error(
        y_prueba,
        predicciones
    )

    rmse = mean_squared_error(
        y_prueba,
        predicciones
    ) ** 0.5

    r2 = r2_score(
        y_prueba,
        predicciones
    )

    print("\n" + "=" * 60)
    print("EVALUACIÓN DEL MODELO")
    print("=" * 60)

    print(f"\nMAE: {mae:.2f} toneladas")
    print(f"RMSE: {rmse:.2f} toneladas")
    print(f"R²: {r2:.4f}")

    return predicciones


def guardar_modelo(modelo, columnas):
    """Guarda el modelo y las columnas utilizadas."""

    paquete = {
        "modelo": modelo,
        "columnas": columnas
    }

    joblib.dump(
        paquete,
        ARCHIVO_MODELO
    )

    print("\nModelo guardado correctamente.")
    print(f"Archivo: {ARCHIVO_MODELO}")


def main():

    datos = cargar_datos()

    if datos is None:
        return

    datos = preparar_datos(datos)

    (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba
    ) = dividir_datos(datos)

    print(
        f"\nRegistros para entrenamiento: "
        f"{len(X_entrenamiento)}"
    )

    print(
        f"Registros para prueba: "
        f"{len(X_prueba)}"
    )

    modelo = entrenar_modelo(
        X_entrenamiento,
        y_entrenamiento
    )

    print("\nModelo Random Forest entrenado correctamente.")

    predicciones = evaluar_modelo(
        modelo,
        X_prueba,
        y_prueba
    )

    guardar_modelo(
        modelo,
        X_entrenamiento.columns.tolist()
    )


if __name__ == "__main__":
    main()