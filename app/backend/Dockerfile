# Imagen base
FROM tensorflow/serving:2.15.1

# Directorio dentro de la imagen en el que se está trabajando
WORKDIR /models

# Se copia el modelo de la ruta local al directorio 'models/sentiment_classifier' dentro de la imagen
COPY mlflow/mlruns/413953086926394230/025e1ff6974f412c898b91aeac09e127/artifacts/model/data/model/ ./sentiment_classifier

# Se configura como variable de entorno la clave 'MODEL_NAME' y el valor 'sentiment_classifier' (nombre igual que la carpeta anterior)
ENV MODEL_NAME=sentiment_classifier

# Se expone el puerto 8501 ya que TensorFlow Serving expone su API REST en este puerto
EXPOSE 8501

# Comprobación de funcionamiento en el localhost de la imagen en el puerto 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health