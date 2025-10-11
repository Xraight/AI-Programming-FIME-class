# AI-Programming-FIME-class
Repository created to storage all the homeworks and all related documents about AI Programming, third semester class in FIME UANL

# Fundamental 5
### 📊 Proyecto de Preprocesamiento de Datos de League of Legends

#### 📝 Descripción del Proyecto

Este proyecto consiste en un script de Python que automatiza el preprocesamiento de un conjunto de datos de partidas de League of Legends (`games.csv`). El objetivo es transformar los datos crudos en un formato limpio, normalizado y listo para ser utilizado en modelos de Machine Learning para predecir el ganador de una partida.

El proceso incluye:
* Carga segura de datos.
* Codificación de variables categóricas (`firstBlood`, `firstTower`, etc.) usando One-Hot Encoding.
* Normalización de variables numéricas (`gameDuration`) con Min-Max Scaling.
* División del conjunto de datos en entrenamiento, validación y prueba.
* Exportación del conjunto de entrenamiento procesado a un nuevo archivo CSV.
