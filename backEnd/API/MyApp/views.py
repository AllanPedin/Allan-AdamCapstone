
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
                    "teamName1": "Atlanta Hawks",
                    "teamName2": "New York Knicks",
                    "winnerIsTeam1": False
                },    
                {
                    "teamName1": "Chicago Bulls",
                    "teamName2": "Miami Heat",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Detroit Pistons",
                    "teamName2": "Philadelphia 76ers",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "Dallas Mavericks",
                    "teamName2": "Denver Nuggets",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Boston Celtics",
                    "teamName2": "Indiana Pacers",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Brooklyn Nets",
                    "teamName2": "Los Angeles Lakers",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Chicago Bulls",
                    "teamName2": "Cleveland Cavaliers",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Golden State Warriors",
                    "teamName2": "Los Angeles Clippers",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "Houston Rockets",
                    "teamName2": "Minnesota Timberwolves",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "San Antonio Spurs",
                    "teamName2": "Dallas Mavericks",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Memphis Grizzlies",
                    "teamName2": "Orlando Magic",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "Phoenix Suns",
                    "teamName2": "Portland Trailblazers",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "Washington Wizards",
                    "teamName2": "New York Knicks",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Milwaukee Bucks",
                    "teamName2": "Denver Nuggets",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "Toronto Rapters",
                    "teamName2": "Utah Jazz",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Sacramento Kings",
                    "teamName2": "Toronto Raptors",
                    "winnerIsTeam1": False
                },
                {
                    "teamName1": "New Orleans Pelicans",
                    "teamName2": "Minnesota Timberwolves",
                    "winnerIsTeam1": True
                },
                {
                    "teamName1": "Oklahoma City Thunder",
                    "teamName2": "Boston Celtics",
                    "winnerIsTeam1": True
                }
            ]
        }
        return JsonResponse(data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
