import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from sqlite3.dbapi2 import DateFromTicks
import time
from keras.models import Sequential
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense

def prepare_data(data, n_steps):
    X, y = [], []
    for i in range(len(data)):
        end_ix = i + n_steps
        if end_ix > len(data)-1:
            break
        seq_x, seq_y = data[i:end_ix], data[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

bitcoin_prices = [float(i) for i in range(100, 2000)]
n_steps = 100


train_size = int(len(bitcoin_prices) * 0.8)
train_data, val_data = bitcoin_prices[:train_size], bitcoin_prices[train_size:]


X_train, y_train = prepare_data(train_data, n_steps)
X_val, y_val = prepare_data(val_data, n_steps)

# МоДелька
model = Sequential()
model.add(SimpleRNN(50, activation='relu', input_shape=(n_steps, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Обучалка
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_val = X_val.reshape((X_val.shape[0], X_val.shape[1], 1))
history = model.fit(X_train, y_train, epochs=20, verbose=0, validation_data=(X_val, y_val))

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='validation')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

# ЕБЕМ
x_input = np.array(bitcoin_prices[-n_steps:])
x_input = x_input.reshape((1, n_steps, 1))
yhat = model.predict(x_input, verbose=0)
print(f'Поднятие лаве: {yhat[0]}')
