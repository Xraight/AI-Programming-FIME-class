import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def evaluate_performance(model, X_test, y_test):
    """
    Imprime métricas y muestra la matriz de confusión.
    """
    print("\n--- Evaluando Resultados ---")
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"Precisión (Accuracy): {acc:.2f}")
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))
    
    # Matriz de Confusión
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix(y_test, y_pred, labels=model.classes_), 
                annot=True, fmt='d', cmap='Blues',
                xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title('Matriz de Confusión')
    plt.ylabel('Real')
    plt.xlabel('Predicción')
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Genera gráficas individuales de importancia de variables por rol.
    """
    print("\nGenerando gráficas de importancia...")
    coefs = model.coef_
    classes = model.classes_

    for i, role in enumerate(classes):
        role_coefs = coefs[i]
        
        # Crear DataFrame para ordenar
        coef_df = pd.DataFrame({'Variable': feature_names, 'Coeficiente': role_coefs})
        coef_df = coef_df.sort_values(by='Coeficiente', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Coeficiente', y='Variable', data=coef_df, palette='viridis')
        plt.title(f'Importancia de Variables para: {role}')
        plt.xlabel('Peso (Impacto)')
        plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
        plt.tight_layout()
        plt.show()