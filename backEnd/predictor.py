from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

# fashion_mnist = keras.datasets.fashion_mnist

# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_games = [1,2] #not sure what the format this is yet
train_labels = [1,2]
test_games = [1,2]
test_labels = [1,2]

class_names = ['Win', 'Lose']#left side wins or left side loses

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='sigmoid'),#activation function sigmoid is a classic
    keras.layers.Dense(10, activation='softmax')#dunno what a softma is
])
