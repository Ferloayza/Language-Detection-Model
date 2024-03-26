# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:33:15 2024

@author: ferna
"""

# Importacion de Librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import seaborn as sns
from string import punctuation
from tensorflow.keras import layers, models


from keras.models import Sequential
from keras.layers import Dense


# Importacion del conjunto de datos
dataset = pd.read_csv('C:/Users/ferna/OneDrive/Documentos/Data science/Language predicting/Database/Language Detection.csv')

#Removing punctuation
def removePunctuation(text):
    clean_text =""

    for i in text:
        if i not in punctuation:
            clean_text+=i
    return clean_text
dataset['clean_text']=dataset['Text'].apply(lambda x:removePunctuation(x.lower()))

text = dataset['clean_text']
language = dataset['Language']

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

vectorizer = CountVectorizer()
label_encoder = LabelEncoder()

text_v = vectorizer.fit_transform(text)
language_v = label_encoder.fit_transform(language)

from sklearn.naive_bayes import MultinomialNB 
model = MultinomialNB()
model.fit(text_v,language_v)

def language_detector(input_xlanguage):
    
    input_xlanguage_v = vectorizer.transform([input_xlanguage])

    language_detected = (model.predict(input_xlanguage_v)[0])

    return language_detected

from googletrans import Translator
translater = Translator()

def predict(input_text):
    
    predicted_language = label_encoder.inverse_transform((language_detector(input_text)).reshape(-1))
    translation = translater.translate(input_text, dest= "en")
    print(f"The predicted language is: {predicted_language} and it says ({translation.text})")
    
predict("Hola esto es una prueba")
predict("Hallo, das ist ein Test")
predict("Привет, это тест")
predict("Γεια σας αυτό είναι ένα τεστ")





