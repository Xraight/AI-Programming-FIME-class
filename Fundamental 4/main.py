# main.py

# 1. Importar las funciones de nuestros módulos
from data_loader import load_data
from feature_engineering import encode_categorical_features, normalize_numerical_feature
from data_processor import split_dataset, export_dataset

def main():
    """
    Función principal para ejecutar el pipeline de preprocesamiento de datos.
    """
    # --- Configuración ---
    INPUT_FILE = r'C:\Users\sergi\.anaconda\Fundamental 5\AI-Programming-FIME-class\Fundamental 5\games.csv'
    OUTPUT_FILE = 'training_dataset_mejorado.csv'
    
    CATEGORICAL_FEATURES = [
        'firstBlood', 'firstTower', 'firstInhibitor',
        'firstBaron', 'firstDragon', 'firstRiftHerald'
    ]
    NUMERICAL_FEATURE_TO_NORM = 'gameDuration'
    TARGET_COLUMN = 'winner'

    # --- Pipeline de ejecución ---
    
    # 1) Cargar datos
    df = load_data(INPUT_FILE)
    if df is None:
        return # Detener la ejecución si el archivo no se carga

    # 2) Ingeniería de características
    df, ohe_cols = encode_categorical_features(df, CATEGORICAL_FEATURES)
    df = normalize_numerical_feature(df, NUMERICAL_FEATURE_TO_NORM)

    # 3) División de datos
    final_features = [f'{NUMERICAL_FEATURE_TO_NORM}_norm'] + ohe_cols
    
    X_train, _, _, y_train, _, _ = split_dataset(
        df=df,
        feature_columns=final_features,
        target_column=TARGET_COLUMN
    )

    # 4) Exportar el conjunto de entrenamiento
    export_dataset(X_train, y_train, final_features, OUTPUT_FILE)


if __name__ == "__main__":
    main()