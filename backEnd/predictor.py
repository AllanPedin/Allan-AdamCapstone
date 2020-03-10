from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# import dataImporter as data
import TestData as data

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

# fashion_mnist = keras.datasets.fashion_mnist

# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# print(train_images)
# print("---------")
# print(train_images[1])
# print(train_labels)
# print("---------")
# print(len(train_labels))
# print(len(train_images))
train_games = data.getTrainingGames()
train_labels = data.getTrainingLabels()
test_games = data.getTestGame()
test_labels = [1,2]

class_names = ['Win', 'Lose']#left side wins or left side loses

model = keras.Sequential([
    # keras.layers.Flatten(input_shape=(2, 19)),
    keras.layers.Dense(128, activation='sigmoid'),#activation function sigmoid is a classic
    # keras.layers.Dense(10, activation='softmax')#dunno what a softma is
])

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

model.fit(train_games, train_labels, epochs=10) #epochs = times to run over same data

#train
# test_loss, test_acc = model.evaluate(test_games,  test_labels, verbose=2)

# print('\nTest accuracy:', test_acc)


#predict on test data
predictions = model.predict(test_games)

predictions[0]#see what it predicted

