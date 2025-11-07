# data_loader.py

import pandas as pd

def load_data(file_path):
    """
    Carga un conjunto de datos desde una ruta de archivo CSV.

    Args:
        file_path (str): La ruta al archivo CSV.

    Returns:
        pandas.DataFrame: El DataFrame cargado o None si el archivo no se encuentra.
    """
    print(f"=== Cargando datos de '{file_path}' ===")
    try:
        df = pd.read_csv(file_path)
        print("El dataset se ha cargado correctamente.")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'.")
        return None