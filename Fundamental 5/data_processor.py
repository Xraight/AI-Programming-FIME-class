# data_processor.py

import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(df, feature_columns, target_column, test_size=0.2, val_size=0.5, random_state=42):
    """
    Divide el DataFrame en conjuntos de entrenamiento, validación y prueba.

    Args:
        df (pandas.DataFrame): El DataFrame completo.
        feature_columns (list): Lista de columnas a usar como características (X).
        target_column (str): El nombre de la columna objetivo (y).
        test_size (float): Proporción para la primera división (entrenamiento vs temporal).
        val_size (float): Proporción para dividir el temporal (validación vs prueba).
        random_state (int): Semilla para la aleatoriedad.

    Returns:
        tuple: Una tupla con los conjuntos X_train, X_val, X_test, y_train, y_val, y_test.
    """
    print("\n=== 4) Dividiendo en conjuntos de entrenamiento, validación y prueba ===")
    X = df[feature_columns].values
    y = df[target_column].values

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=test_size, random_state=random_state)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=val_size, random_state=random_state)
    
    print(f"Tamaño del conjunto de entrenamiento: {len(X_train)} filas")
    print(f"Tamaño del conjunto de validación: {len(X_val)} filas")
    print(f"Tamaño del conjunto de prueba: {len(X_test)} filas")
    
    return X_train, X_val, X_test, y_train, y_val, y_test

def export_dataset(X_data, y_data, columns, filename):
    """
    Exporta un conjunto de datos a un archivo CSV.

    Args:
        X_data (np.array): Las características del conjunto de datos.
        y_data (np.array): Las etiquetas del conjunto de datos.
        columns (list): Los nombres de las columnas de características.
        filename (str): El nombre del archivo de salida.
    """
    print(f"\n=== 5) Exportando el conjunto a '{filename}' ===")
    df_export = pd.DataFrame(X_data, columns=columns)
    df_export['winner'] = y_data
    
    df_export.to_csv(filename, index=False)
    print(f"\n¡Éxito! El conjunto ha sido exportado.")
    print("Primeras filas del archivo exportado:")
    print(df_export.head())