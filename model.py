from sklearn.neural_network import MLPClassifier

def entrenar_modelo(X_train, y_train):
    """Configura y entrena la Red Neuronal."""
    print("🔄 Entrenando el modelo (esto puede tardar unos segundos)...")
    
    modelo = MLPClassifier(hidden_layer_sizes=(16, 8), 
                           activation='relu', 
                           solver='adam', 
                           max_iter=1000, 
                           random_state=42)
    
    modelo.fit(X_train, y_train)
    print("✅ Entrenamiento completado.")
    return modelo