# Importamos las funciones de nuestros archivos
from data_loader import cargar_datos
# AQUÍ ESTÁ EL CAMBIO: ahora importamos de 'procesamiento' en lugar de 'preprocessing'
from procesamiento import preprocesar_datos, preparar_train_test
from model import entrenar_modelo
from evaluation import evaluar_modelo

def main():
    # 1. Cargar
    archivo = 'high_diamond_ranked_10min.csv'
    df = cargar_datos(archivo)
    
    if df is not None:
        # 2. Procesar
        X, y = preprocesar_datos(df)
        
        # 3. Preparar
        X_train, X_test, y_train, y_test = preparar_train_test(X, y)
        
        # 4. Entrenar
        modelo = entrenar_modelo(X_train, y_train)
        
        # 5. Evaluar
        evaluar_modelo(modelo, X_test, y_test)

if __name__ == "__main__":
    main()