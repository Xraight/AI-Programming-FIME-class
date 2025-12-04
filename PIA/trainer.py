from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    """
    Inicializa y entrena el modelo de Regresión Logística.
    """
    print("Entrenando modelo...")
    
    model = LogisticRegression(
        multi_class='multinomial', 
        solver='lbfgs', 
        max_iter=2000, 
        random_state=42
    )
    
    model.fit(X_train, y_train)
    print("Entrenamiento completado.")
    return model