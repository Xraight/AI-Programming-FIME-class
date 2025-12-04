import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Realiza One Hot Encoding, Split y Scaling.
    Retorna los sets de entrenamiento/test y los nombres de las columnas.
    """
    print("Preprocesando datos...")
    
    # 1. One Hot Encoding para FlashKeybind
    df = pd.get_dummies(df, columns=['FlashKeybind'], drop_first=True)
    
    # 2. Separar X e y
    X = df.drop('Position', axis=1)
    y = df['Position']
    feature_names = X.columns # Guardamos nombres para las gráficas
    
    # 3. Split (Estratificado para mantener balance de roles)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 4. Escalar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, feature_names