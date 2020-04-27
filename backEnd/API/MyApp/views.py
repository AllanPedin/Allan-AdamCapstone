
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
@api_view(['GET'])
#import predictor
#predict games - put games in same format made for training & test data
#should predict on it

def gamePredictions(request):
    try:
        data = {
            'games':[ #call to get predictions from NN
                {
                    "teamName1": "Milwaukee Bucks",
                    "teamName2": "Houston Rockets",
                    "winnerIsTeam1": True
                },    
                {
                    "teamName1": "LA Clippers",
                    "teamName2": "Washington Wizards",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Dallas Mavericks",
                    "teamName2": "New Orleans Pelicans",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Los Angeles Lakers",
                    "teamName2": "Portland Trail Blazers",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Minnesota Timberwolves",
                    "teamName2": "San Antonio Spurs",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Boston Celtics",
                    "teamName2": "Toronto Raptors",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Memphis Grizzlies",
                    "teamName2": "Phoenix Suns",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Miami Heat",
                    "teamName2": "Atlanta Hawks",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Utah Jazz",
                    "teamName2": "Brooklyn Nets",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Oklahoma City Thunder",
                    "teamName2": "Denver Nuggets",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Philadelphia 76ers",
                    "teamName2": "Indiana Pacers",
                    "winnerIsTeam1": True
                }
            ]
        }
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
