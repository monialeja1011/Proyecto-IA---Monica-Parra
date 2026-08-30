import pandas as pd
import joblib


ARCHIVO_MODELO = "data/modelo_cafetero.pkl"


def cargar_modelo():
    """Carga el modelo de Machine Learning."""

    try:
        paquete = joblib.load(ARCHIVO_MODELO)

        modelo = paquete["modelo"]
        columnas = paquete["columnas"]

        return modelo, columnas

    except FileNotFoundError:
        print("Error: no se encontró el modelo.")
        print("Ejecute primero:")
        print("python src/entrenar_modelo.py")
        return None, None


def solicitar_datos():
    """Solicita al usuario los datos del cultivo."""

    print("\n" + "=" * 60)
    print("☕ PREDICCIÓN DE PRODUCCIÓN CAFETERA")
    print("=" * 60)

    print("\nIngrese la información del cultivo:\n")

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
    """Prepara los datos para que tengan el mismo formato del entrenamiento."""

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
    """Realiza la predicción de producción."""

    prediccion = modelo.predict(datos)

    return prediccion[0]


def mostrar_resultado(produccion):
    """Muestra el resultado de la predicción."""

    print("\n" + "=" * 60)
    print("RESULTADO DE LA PREDICCIÓN")
    print("=" * 60)

    print(
        f"\nProducción estimada: "
        f"{produccion:.2f} toneladas"
    )

    print("\nLa predicción fue realizada")
    print("utilizando un modelo Random Forest.")

    print("\n" + "=" * 60)


def main():

    modelo, columnas = cargar_modelo()

    if modelo is None:
        return

    (
        municipio,
        año,
        hectareas_sembradas,
        hectareas_cosechadas
    ) = solicitar_datos()

    datos = preparar_datos(
        municipio,
        año,
        hectareas_sembradas,
        hectareas_cosechadas,
        columnas
    )

    produccion = realizar_prediccion(
        modelo,
        datos
    )

    mostrar_resultado(produccion)


if __name__ == "__main__":
    main()
