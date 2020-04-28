
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

import json
import csv

import numpy as np
from numpy import load

games = load("matchups.npy", allow_pickle=True)
deletables = []
for game in games:
    if "vs." in game[2]:
        gameStr = game[2][15:]
        removeGameStr = gameStr[9:] + " @ " + gameStr[:3]
        for i in range(len(games)):
            if removeGameStr in games[i][2]:
                print("eeeeeee")
                deletables.append( i )
                break
print(deletables)
games = np.delete(games, deletables,0)
print(games)
###################
import tensorflow as tf
from tensorflow import keras

model = tf.keras.models.load_model('./Models/myModel0.5740741')#edit model
gamesToPredict = []
gameStrings = []
for game in games:
    gamesToPredict.append(game[0])
    gameStrings.append(game[2])
predictions = model.predict(gamesToPredict)
print(predictions)
print(gameStrings)
dataToSend = []
for i in range(len(gamesToPredict)):
    winner = True
    if predictions[i][0] < predictions[i][1]:
        winner = False
    dataToSend.append({
        "teamName1": gameStrings[i][15:18],
        "teamName2": gameStrings[i][23:],
        "winnerIsTeam1": winner,
        "date": gameStrings[i][:15]
    })

@api_view(['GET'])
#import predictor
#predict games - put games in same format made for training & test data
#should predict on it
def gamePredictions(request):
    try:
        data = {
            'games': dataToSend
        }
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)