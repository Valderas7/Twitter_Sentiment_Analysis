# Librerías
import json
import streamlit as st
import requests

# Título de la Web App con cabecera H2
st.markdown("<h2 style='text-align: center; color: black;'> Análisis de sentimientos de Tweets </h2>",
            unsafe_allow_html=True)

# Información de que el backend está en TF Serving
st.write('''Obtén los análisis de sentimientos de `tweets`. Esta interfaz de `Streamlit` usa el servicio de `TensorFlow Serving` 
como `backend` realizando peticiones `POST` a dicho servicio.''')

# Este texto vacío es simplemente para crear espacio entre el texto de arriba y el que irá debajo
st.text("")

# Se guarda en una variable la URL local donde se realizan las peticiones 'POST' al modelo para obtener las predicciones
api_url = "http://localhost:8501/v1/models/sentiment_classifier:predict"

# No se carga el modelo porque está en TensorFlow Serving

# Se crea un botón de entrada de texto
title = st.text_input(label="Tweet a analizar", value="")

# Se crea un cuerpo JSON de entrada para enviar como solicitud 'POST' a TensorFlow Serving siguiendo su formato establecido de
# usar 'instances' como clave y los valores a inferir
# Se envía como valor a inferir el texto de entrada introducido en el botón de entrada de texto
inputs = {"instances": [[title]]}

# Una vez creado el objeto JSON, se envía la petición 'POST' con este objeto a la URL de la API, almacenando la respuesta JSON
# en una variable
response = requests.post(url=api_url, json=inputs).json()

# Se obtiene el valor de la clave 'predictions' del objeto JSON, almacenándolo en una variable
value = response['predictions'][0][0]

# Si el valor es igual o mayor de 0.5 el sentimiento es positivo, sino, es negativo
value_string = 'positivo' if value >= 0.5 else 'negativo'

# Se imprime la predicción obtenida con la petición 'POST' con una cabecera H4
st.write("<h4 style='text-align: center; color: black;'> El sentimiento del tweet es " +
         value_string + "</h4>", unsafe_allow_html=True)