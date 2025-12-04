# Importamos nuestras funciones desde los otros archivos
from data_loader import load_data
from preprocessor import preprocess_data
from trainer import train_model
from evaluator import evaluate_performance, plot_feature_importance

def main():
    # 1. Configuración
    FILE_PATH = r'C:\Users\sergi\.anaconda\AI-Programming-FIME-class\PIA\player_statistics_cleaned_final.csv'
    
    # 2. Ejecución Modular
    try:
        # Cargar
        df = load_data(FILE_PATH)
        
        # Preprocesar
        X_train, X_test, y_train, y_test, feature_names = preprocess_data(df)
        
        # Entrenar
        model = train_model(X_train, y_train)
        
        # Evaluar
        evaluate_performance(model, X_test, y_test)
        
        # Visualizar Importancia
        plot_feature_importance(model, feature_names)
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()