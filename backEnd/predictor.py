from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# import dataImporter as data
import dataAverager as data

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
print(train_images.shape)
print(train_labels.shape)
# print(train_images)
# print("---------")
# print(train_images[1])
# print(train_labels)
# print("---------")
# print(len(train_labels))
# print(len(train_images))
train_games =tf.convert_to_tensor( data.getTrainingGames() )
train_labels = tf.convert_to_tensor(data.getTrainingLabels() )
test_games = tf.convert_to_tensor( data.getTestGames() )
test_labels = tf.convert_to_tensor( data.getTestLabels() )

print(train_labels.shape)
print (train_games.shape)
class_names = ['Win', 'Lose']#left side wins or left side loses

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(2, 20)),
    keras.layers.Dense(20, activation='relu'),
    keras.layers.Dense(2)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_games, train_labels, epochs=10) #epochs = times to run over same data

#train
# test_loss, test_acc = model.evaluate(test_games,  test_labels, verbose=2)

# print('\nTest accuracy:', test_acc)

test_loss, test_acc = model.evaluate(test_games,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)


#predict on test data
predictions = model.predict(test_games)

print(predictions)#see what it predicted
print(type(predictions[0]))


def predict(games):
    TFGames = tf.convert_to_tensor(games)
    return model.predict(TFGames)

predictions = predict(data.getGamesFromCSV("Games_to_predict.csv"))
print(predictions)
