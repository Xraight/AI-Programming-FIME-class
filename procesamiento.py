from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocesar_datos(df):
    """
    Selecciona las columnas, elimina redundancia y define el objetivo.
    """
    # Objetivo: 0 = Gana Blue, 1 = Gana Red
    y = 1 - df['blueWins']
    
    # Selección manual de variables
    features_to_use = [
        'blueGoldDiff', 'blueExperienceDiff',
        'blueTotalGold', 'blueTotalExperience',
        'blueKills', 'blueDeaths', 'blueAssists',
        'blueTotalMinionsKilled', 'blueTotalJungleMinionsKilled',
        'blueDragons', 'blueWardsPlaced',
        'redTotalGold', 'redTotalExperience',
        'redTotalMinionsKilled', 'redTotalJungleMinionsKilled',
        'redDragons', 'redWardsPlaced'
    ]
    
    X = df[features_to_use]
    print(f"✅ Preprocesamiento listo. Variables seleccionadas: {X.shape[1]}")
    return X, y

def preparar_train_test(X, y):
    """
    Divide en entrenamiento/prueba y escala los datos.
    """
    # Dividir
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Escalar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test