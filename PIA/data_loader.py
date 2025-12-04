import pandas as pd
import os

def load_data(filepath):
    """
    Carga el dataset desde una ruta especifica.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo no se encuentra en: {filepath}")
    
    print(f"Cargando datos desde {filepath}...")
    df = pd.read_csv(filepath)
    return df