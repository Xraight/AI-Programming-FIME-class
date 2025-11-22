# 🔮 Predicción de Partidas de League of Legends (Ranked Diamante)

Este proyecto implementa un modelo de **Inteligencia Artificial (Red Neuronal)** capaz de predecir el equipo ganador de una partida de League of Legends basándose únicamente en las estadísticas de los primeros **10 minutos** de juego.

El modelo utiliza un dataset de partidas de alto ELO (Diamante I a Master) y resuelve un problema de **Clasificación Binaria**.

## 📂 Estructura del Proyecto

El código ha sido modularizado siguiendo buenas prácticas de ingeniería de software para facilitar su lectura, mantenimiento y escalabilidad:

```text
📁 LoL-Prediction-AI/
│
├── 📄 high_diamond_ranked_10min.csv  # Dataset (Fuente de datos)
├── 📄 main.py                        # Archivo principal (Ejecutar este)
├── 📄 data_loader.py                 # Módulo de carga de datos
├── 📄 procesamiento.py               # Limpieza, selección de features y escalado
├── 📄 model.py                       # Configuración de la Red Neuronal (MLP)
├── 📄 evaluation.py                  # Generación de métricas y gráficas
└── 📄 README.md                      # Documentación del proyecto