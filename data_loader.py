import pandas as pd

def cargar_datos(ruta_archivo):
    """Carga el CSV y devuelve un DataFrame."""
    try:
        df = pd.read_csv("high_diamond_ranked_10min.csv")
        print(f"✅ Datos cargados correctamente: {df.shape[0]} partidas encontradas.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        return None