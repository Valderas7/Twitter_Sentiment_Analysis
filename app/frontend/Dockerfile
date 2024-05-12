# Imagen base
FROM python:3.9-slim

# Directorio dentro de la imagen en el que se está trabajando
WORKDIR /app

# Se copia el contenido de la carpeta 'frontend' local (código y 'requirements.txt') al directorio 'app' de la imagen
COPY app/frontend/requirements.txt app/frontend/app.py ./

# Se actualiza la imagen y se instalan las librerías del 'requirements.txt'
RUN apt-get update && pip install -r requirements.txt

# Se expone el puerto 8502 ya que será en éste donde se servirá la aplicación
EXPOSE 8502

# Comprobación de funcionamiento en el localhost de la imagen en el puerto 8502
HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

# Se ejecuta la APP de streamlit con el código copiado en la imagen especificando la IP (127.0.0.1) y el puerto (8502)
# donde se servirá
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0"]