# AI-Programming-FIME-class
Repositorio creado para el almacenamiento de todas las tareas y archivos relacionados con la Programación para Inteligencia Artificial, materia del tercer semestre de la Ing. en Inteligencia Artificial,  FIME UANL.

# Fundamental 5
## 📊 Proyecto de Preprocesamiento de Datos de League of Legends

### 📝 Descripción del Proyecto

Este proyecto consiste en un script de Python que automatiza el preprocesamiento de un conjunto de datos de partidas de League of Legends (`games.csv`). El objetivo es transformar los datos crudos en un formato limpio, normalizado y listo para ser utilizado en modelos de Machine Learning para predecir el ganador de una partida.

El proceso incluye:
* **Carga de Datos**: Lee un archivo `.csv` desde una ruta especificada.
* **Ingeniería de Características**:
    * Aplica **codificación One-Hot** a variables categóricas (`firstBlood`, `firstTower`, etc.) para convertirlas en un formato numérico.
    * Realiza **normalización Min-Max** a características numéricas (`gameDuration`) para escalar sus valores entre 0 y 1.
* **División de Datos**: Separa el conjunto de datos procesado en subconjuntos de entrenamiento, validación y prueba.
* **Exportación**: Guarda el conjunto de datos de entrenamiento ya procesado en un nuevo archivo `.csv`.

### 🚀 Instalación y Ejecución

Para configurar y ejecutar este proyecto en tu máquina local, sigue los siguientes pasos. Se requiere tener **Anaconda** instalado.
El proyecto utiliza un archivo `environment.yml` para asegurar que todas las dependencias se instalen correctamente.

Usa este archivo para crear el entorno virtual de Conda. Este comando instalará la versión correcta de Python y todas las librerías necesarias.
```
conda env create -f environment.yml
```
Puedes iniciar tu entorno virtual desde la interfaz gráfica de conda; si no, puedes utilizar
```
conda activate preproceso-env
```
Notarás que el nombre del entorno (preproceso-env) aparece al inicio de la línea en tu terminal.

#### 🛠️ Cómo Usar el Pipeline

1. Crea una carpeta llamada data en la raíz de tu proyecto.

2. Coloca tu archivo `games.csv` dentro de la carpeta data. (En la carpeta se incluye el database utilizado para este ejercicio)

3. Abre el archivo `main.py` y ajusta las variables en la sección de Configuración para que coincidan con tus nombres de archivo y columnas deseadas.
```
    # --- Configuración ---
    # Asegúrate de que esta ruta apunte a tu archivo de entrada
    INPUT_FILE = 'data/games.csv'
```
4. Ejecutar el script
   Con el entorno activado y las rutas configuradas, ejecuta el script principal desde tu terminal.
```
python main.py
```
Al finalizar, se creará un nuevo archivo llamado `training_dataset_mejorado.csv` en la carpeta principal del proyecto, el cual contiene los datos listos para el entrenamiento de un modelo.
