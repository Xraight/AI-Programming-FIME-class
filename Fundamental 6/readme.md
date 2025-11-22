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
```
## ⚙️ Requisitos e Instalación

Para ejecutar este proyecto necesitas las dependencias expresadas en el ```enviroment.yml ```y las siguientes librerías de ciencia de datos. Puedes instalarlas ejecutando:

```
pip install pandas scikit-learn matplotlib seaborn
```

## 🚀 Cómo Ejecutar

- Asegúrate de que todos los archivos ```.py``` y el dataset ```.csv``` estén en la misma carpeta.

- Abre tu terminal en dicha carpeta.

- Ejecuta el archivo principal:

```
python main.py
```

El script ejecutará automáticamente el pipeline completo:

Carga de datos. -> Preprocesamiento (Limpieza y Selección). -> Entrenamiento de la Red Neuronal. -> Evaluación y visualización de resultados.

## 🧠 Metodología y Modelo

**1. Definición del Problema**

- **Tipo**: Clasificación Binaria (Aprendizaje Supervisado).

- **Entrada**: Estadísticas al minuto 10 (Oro, Experiencia, Kills, Dragones, etc.).

- **Salida**: ````0```` (Gana Equipo Azul) o ````1```` (Gana Equipo Rojo).

**2. Selección de Características (Feature Engineering)**

El dataset original contiene 40 variables. Tras un análisis de correlación, se redujeron a las ~17 más relevantes para evitar la **multicolinealidad** (redundancia de datos) y el **ruido**.

- **Variables Clave**: ````blueGoldDiff```` y ````blueExperienceDiff```` (los predictores más fuertes).

- **Limpieza**: Se eliminaron variables espejo del equipo rojo (ej. ````redDeaths```` es idéntica a ````blueKills````) y variables calculadas redundantes.

**3. Arquitectura del Modelo**

Se utiliza un Perceptrón Multicapa (MLPClassifier) de la librería ````scikit-learn```` con la siguiente configuración:

- **Capas Ocultas**: 2 capas densas (16 y 8 neuronas).

- **Función de Activación**: ReLU (Rectified Linear Unit).

- **Optimizador**: Adam.

- Normalización: Se aplicó ````StandardScaler```` a los datos de entrada para mejorar la convergencia de la red, dado que las magnitudes de las variables varían drásticamente (ej. Oro vs Dragones).

📊 Resultados Esperados

El modelo alcanza una exactitud (**Accuracy**) aproximada del 71% - 72% en el conjunto de prueba.

- **Interpretación**: Predecir el resultado final con solo 10 minutos de información es complejo debido a la naturaleza impredecible del juego (remontadas, errores tardíos). Un 72% es considerado un rendimiento sólido para este dataset específico sin caer en sobreajuste (overfitting).

- **Output Visual**: El programa generará una **Matriz de Confusión** mostrando los aciertos y errores del modelo para cada clase (Gana Blue vs Gana Red).
