import pandas as pd
import joblib
import matplotlib.pyplot as plt


ARCHIVO_MODELO = "data/modelo_cafetero.pkl"
ARCHIVO_DATOS = "data/cafe_valle_limpio.csv"


def cargar_modelo():
    """Carga el modelo entrenado."""

    try:
        paquete = joblib.load(ARCHIVO_MODELO)

        modelo = paquete["modelo"]
        columnas = paquete["columnas"]

        return modelo, columnas

    except FileNotFoundError:
        print("Error: no se encontró el modelo.")
        return None, None


def cargar_datos():
    """Carga los datos históricos."""

    try:
        return pd.read_csv(
            ARCHIVO_DATOS,
            sep=";",
            encoding="utf-8"
        )

    except FileNotFoundError:
        print("Error: no se encontró el dataset.")
        return None


def solicitar_datos():
    """Solicita los datos del cultivo."""

    print("\n" + "=" * 60)
    print("☕ SISTEMA DE PREDICCIÓN DE PRODUCCIÓN CAFETERA")
    print("=" * 60)

    print("\nIngrese los datos para realizar la predicción:\n")

    municipio = input("Municipio: ")

    año = int(
        input("Año a predecir: ")
    )

    hectareas_sembradas = float(
        input("Hectáreas sembradas: ")
    )

    hectareas_cosechadas = float(
        input("Hectáreas cosechadas: ")
    )

    return (
        municipio,
        año,
        hectareas_sembradas,
        hectareas_cosechadas
    )


def preparar_datos(
    municipio,
    año,
    hectareas_sembradas,
    hectareas_cosechadas,
    columnas
):
    """Prepara los datos para el modelo."""

    entrada = pd.DataFrame({
        "Año": [año],
        "Hectareas_sembradas": [hectareas_sembradas],
        "Hectareas_cosechadas": [hectareas_cosechadas],
        "Municipio": [municipio]
    })

    entrada = pd.get_dummies(
        entrada,
        columns=["Municipio"],
        dtype=int
    )

    entrada = entrada.reindex(
        columns=columnas,
        fill_value=0
    )

    return entrada


def realizar_prediccion(modelo, datos):
    """Realiza la predicción."""

    prediccion = modelo.predict(datos)

    return prediccion[0]


def mostrar_resultado(produccion):
    """Muestra el resultado de la predicción."""

    print("\n" + "=" * 60)
    print("RESULTADO DE LA PREDICCIÓN")
    print("=" * 60)

    print(
        f"\n☕ Producción estimada: "
        f"{produccion:.2f} toneladas"
    )

    print("\nModelo utilizado: Random Forest Regressor")

    print("=" * 60)


def crear_grafica(
    datos,
    municipio,
    año_prediccion,
    produccion_predicha
):
    """Guarda una gráfica con la producción histórica y la predicción."""

    historico = datos[
        (datos["Municipio"] == municipio) &
        (datos["Cultivo"].str.contains(
            "Caf",
            case=False,
            na=False
        ))
    ].copy()

    historico = historico.sort_values("Año")

    plt.figure(figsize=(12, 6))

    plt.plot(
        historico["Año"],
        historico["Produccion_toneladas"],
        marker="o",
        label="Producción histórica"
    )

    plt.scatter(
        año_prediccion,
        produccion_predicha,
        s=120,
        label="Predicción"
    )

    plt.title(
        f"Producción de café - {municipio}"
    )

    plt.xlabel("Año")

    plt.ylabel("Producción (toneladas)")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    archivo_grafica = "data/prediccion_cartago.png"

    plt.savefig(
        archivo_grafica,
        dpi=150
    )

    plt.close()

    print("\nGráfica guardada correctamente en:")
    print(archivo_grafica)


def main():

    modelo, columnas = cargar_modelo()

    if modelo is None:
        return

    datos = cargar_datos()

    if datos is None:
        return

    (
        municipio,
        año,
        hectareas_sembradas,
        hectareas_cosechadas
    ) = solicitar_datos()

    entrada = preparar_datos(
        municipio,
        año,
        hectareas_sembradas,
        hectareas_cosechadas,
        columnas
    )

    produccion = realizar_prediccion(
        modelo,
        entrada
    )

    mostrar_resultado(produccion)

    crear_grafica(
        datos,
        municipio,
        año,
        produccion
    )


if __name__ == "__main__":
    main()