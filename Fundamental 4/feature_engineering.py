# feature_engineering.py

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

def encode_categorical_features(df, categorical_features):
    """
    Aplica One-Hot Encoding a las columnas categóricas especificadas.

    Args:
        df (pandas.DataFrame): El DataFrame de entrada.
        categorical_features (list): Lista de nombres de columnas a codificar.

    Returns:
        pandas.DataFrame: El DataFrame con las nuevas columnas codificadas.
        list: La lista de nombres de las nuevas columnas creadas.
    """
    print("\n=== 2) Aplicando One-Hot Encoder ===")
    try:
        # Para versiones más nuevas de scikit-learn
        ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    except TypeError:
        # Para versiones más antiguas de scikit-learn
        ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
        
    ohe_mat = ohe.fit_transform(df[categorical_features])
    ohe_cols = ohe.get_feature_names_out(categorical_features)
    
    df_ohe = pd.DataFrame(ohe_mat, columns=ohe_cols, index=df.index)
    
    # Unimos las nuevas columnas al DataFrame original
    df_processed = pd.concat([df, df_ohe], axis=1)
    
    print(f"Se han creado {len(ohe_cols)} nuevas columnas.")
    return df_processed, list(ohe_cols)

def normalize_numerical_feature(df, column_name):
    """
    Aplica normalización Min-Max a una columna numérica.

    Args:
        df (pandas.DataFrame): El DataFrame de entrada.
        column_name (str): El nombre de la columna a normalizar.

    Returns:
        pandas.DataFrame: El DataFrame con la columna normalizada añadida.
    """
    print("\n=== 3) Aplicando Normalización Min-Max ===")
    scaler = MinMaxScaler()
    new_column_name = f"{column_name}_norm"
    df[[new_column_name]] = scaler.fit_transform(df[[column_name]])
    
    print(f"La columna '{column_name}' ha sido normalizada en '{new_column_name}'.")
    return df