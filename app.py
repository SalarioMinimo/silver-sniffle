import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np


st.title("¿Qué flor es esta? :seedling:")
uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5')


  if label ==0:
    tipo = "Un Tulipán :tulip:"
  elif label ==1:
    tipo = "Un Girasol :sunflower:"
  elif label ==2:
    tipo = "Una Rosa :rose:"
  elif label ==3:
    tipo = "Un Diente de leon"
  elif label ==4:
    tipo = "Una Margarita :blossom:"
  st.title("Esta flor es: " + tipo )
