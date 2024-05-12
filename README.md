# Twitter Sentiment Analysis

En este repositorio se realiza un entrenamiento con `TensorFlow` de un modelo de procesamiento de lenguaje natural (`NLP`) para obtener un modelo que permite analizar los sentimientos de `tweets` en lenguaje inglés.

Los parámetros de la red neuronal, las métricas e incluso el modelo se `logean` automáticamente con `MLflow`.

A partir de aquí se crea una imagen con `Docker` en la que se sirve el modelo entrenado mediante un `endpoint API REST` de `TensorFlow Serving`. Aparte de esto, se crea otra imagen de `Docker` en la que se sirve una aplicación web que realiza solicitudes `POST` al `endpoint API REST` de `TensorFlow Serving` para obtener las predicciones y mostrarlas de forma más estéticas mediante dicha aplicación web.


## Estructura

- **app**: Directorio donde se recopilan los archivos para crear las imágenes de `Docker` y la aplicación web.
    - **backend**: Aquí se encuentra el archivo `Dockerfile` para crear la imagen en la que se sirve el modelo entrenado en la `API REST` de `TensorFlow Serving`.
    - **frontend**: En esta carpeta se encuentra el código de la aplicación web y el `Dockerfile` para crear la imagen en la que se sirve dicha aplicación.


- **data**: Archivo utilizado para realizar el entrenamiento del modelo (ignorado con `.gitignore`).


- **deployment**: Carpeta donde se almacenan los archivos `YAML` para la creación del despliegue y servicio de `Kubernetes`, así como un tutorial sobre como realizar la puesta en producción de la aplicación web y el `endpoint` de `TensorFlow Serving` en el `cluster` local de `Minikube`.


- **img**: Carpeta donde se recopilan un par de imágenes de demostración del proyecto.


- **mlflow**: Directorio donde se recopilan las carpetas por usar `MLflow`. Por tanto, se recopilan los parámetros y métricas de la ejecución realizada en el experimento del proyecto, además de los `artifacts` generados. Es decir, el modelo, sus metadatos, etc.


- **requirements.txt**: Archivo de texto con todas las librerías necesarias de `Python` a instalar para que se pueda ejecutar todo el proyecto.


- **train.ipynb**: `Notebook` en el que se realiza el entrenamiento del modelo con `TensorFlow`, además de explicaciones básicas de como debe ser el procesamiento de datos en un problema básico de procesamiento de lenguaje natural (`NLP`).