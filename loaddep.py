from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences 
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, GlobalMaxPooling1D
from tensorflow.keras.models import Model
import pickle
model = keras.models.load_model('depmod')
text=["I wanna cry all the time"]


# In[6]:


def predict_sentiment1(text):
  print()
  f = open('tokdep','rb')
  tokenizer = pickle.load(f)
  k=[]
  k.append(text)
  T=4388
  print("RESULT: ")
  # preprocessing the given text 
  text_seq = tokenizer.texts_to_sequences(k)
  #print(text_seq)
  text_pad = pad_sequences(text_seq, maxlen=T)
  #print(text_pad)
  # predicting the class
  predicted_sentiment = model.predict(text_pad)
  #print(predicted_sentiment)
  predicted_sentiment = model.predict(text_pad).round()

  if predicted_sentiment == 1.0:
    return 'This post suggests depression'
  else:
    return 'This post does not suggest depression'
  k.pop()
#predict_sentiment(text)


# In[ ]:




