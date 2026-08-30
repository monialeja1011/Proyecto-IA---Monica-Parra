import pandas as pd
import matplotlib.pyplot as plt


ARCHIVO = "data/cafe_valle_limpio.csv"
ARCHIVO_GRAFICA = "data/produccion_cartago.png"


def cargar_datos():
    """Carga los datos limpios del proyecto."""

    try:
        datos = pd.read_csv(
            ARCHIVO,
            sep=";",
            encoding="utf-8"
        )

        return datos

    except FileNotFoundError:
        print("Error: no se encontró el archivo de datos.")
        return None


def obtener_datos_cartago(datos):
    """Filtra los registros de café correspondientes a Cartago."""

    cartago = datos[
        (datos["Municipio"] == "Cartago") &
        (datos["Cultivo"].str.contains("Caf", case=False, na=False))
    ].copy()

    cartago = cartago.sort_values("Año")

    return cartago


def crear_grafica(cartago):
    """Genera la gráfica de producción histórica de Cartago."""

    plt.figure(figsize=(12, 6))

    plt.plot(
        cartago["Año"],
        cartago["Produccion_toneladas"],
        marker="o"
    )

    plt.title(
        "Producción histórica de café en Cartago, Valle"
    )

    plt.xlabel("Año")

    plt.ylabel("Producción (toneladas)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        ARCHIVO_GRAFICA,
        dpi=150
    )

    plt.show()


def main():

    print("=" * 60)
    print("GRÁFICA DE PRODUCCIÓN CAFETERA")
    print("=" * 60)

    datos = cargar_datos()

    if datos is None:
        return

    cartago = obtener_datos_cartago(datos)

    print(f"\nRegistros encontrados: {len(cartago)}")

    if cartago.empty:
        print("No se encontraron datos de café para Cartago.")
        return

    print(
        f"Periodo: "
        f"{cartago['Año'].min()} - {cartago['Año'].max()}"
    )

    print("\nGenerando gráfica...")

    crear_grafica(cartago)

    print("\nGráfica guardada correctamente en:")
    print(ARCHIVO_GRAFICA)


if __name__ == "__main__":
    main()
