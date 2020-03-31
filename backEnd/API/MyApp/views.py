
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
@api_view(['GET'])


def gamePredictions(request):
    try:
        data = {
                'games':[ #call to get predictions from NN
                    {
                        'teamName1': 'dogs',
                        'teamName2': 'cats',
                        'winnerIsTeam1' : True
                    }
                ]
            }
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)