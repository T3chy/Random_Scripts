
import os
import sys
import time
import keras
import heapq
import numpy as np
import tensorflow as tf
from shutil import copyfile
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, Dropout, GRU, TimeDistributed, BatchNormalization
from keras.layers import CuDNNLSTM 
from keras.layers.core import Dense, Activation, Dropout, RepeatVector
from keras.optimizers import RMSprop
# quotes = open('lenin.txt',encoding='utf8').read().lower
quotes = ""
with open('lenin.txt','r') as lenin:
    for quote in lenin:
        quotes = quotes + quote
#tokenizer = Tokenizer(num_words=None, filters='#$%&()*+-<>@[\\]^_`{|}~\t\n', lower = False, split = ' ')
chars = sorted(list(set(quotes)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))
print('Unique Chars:', len(chars))
Sequence_Length = 80
Step_Size = 4
sentences = []
next_chars = []
for i in range(0, len(quotes) - Sequence_Length, Step_Size):
    sentences.append(quotes[i: i + Sequence_Length])
    next_chars.append(quotes[i + Sequence_Length])
X = np.zeros((len(sentences), Sequence_Length, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

model = Sequential()

model.add(LSTM(len(chars) * 5, input_shape=(Sequence_Length, len(chars))))
model.add(BatchNormalization())
model.add(Activation('selu'))

model.add(Dense(len(chars) * 2))
model.add(BatchNormalization())
model.add(Activation('selu'))

model.add(Dense(len(chars) * 2))
model.add(BatchNormalization())
model.add(Activation('selu'))

model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

model.fit(X, y, validation_split=0.05, batch_size=124, epochs=4, shuffle=True)
model.save('leninv1.h5')