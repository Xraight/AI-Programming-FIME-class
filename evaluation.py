import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluar_modelo(modelo, X_test, y_test):
    """Genera predicciones, métricas y la matriz de confusión."""
    # Predicciones
    predictions = modelo.predict(X_test)
    
    # Métricas numéricas
    acc = accuracy_score(y_test, predictions)
    print("\n" + "="*40)
    print(f"🎯 EXACTITUD DEL MODELO: {acc*100:.2f}%")
    print("="*40)
    print("\nReporte Detallado:")
    print(classification_report(y_test, predictions, target_names=['Gana Blue', 'Gana Red']))
    
    # Gráfica Matriz de Confusión
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', cbar=False)
    plt.title('Matriz de Confusión: Predicción de Victoria')
    plt.xlabel('Predicción')
    plt.ylabel('Realidad')
    plt.xticks([0.5, 1.5], ['Gana Blue', 'Gana Red'])
    plt.yticks([0.5, 1.5], ['Gana Blue', 'Gana Red'])
    plt.tight_layout()
    plt.show()