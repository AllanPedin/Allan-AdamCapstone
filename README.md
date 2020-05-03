# Allan-AdamCapstone
Neural Net that analyzes and predicts the winner of basketball games.

# Backend
###### How to run
- download python 3.7 as well as pip, 3.8 does not support tensor flow : https://www.python.org/downloads/
- cd Allan-AdamCapstone/backEnd/API/
  - pip install Django
  - pip install django-cors-headers
  - pip install djangorestframework
  - pip install django-common
  - pip install numpy
  - pip install tensorflow
- run local:
  - python manage.py runserver
- run on server (make sure your aws instance has all ports opened and no firewalls setup)
  - python manage.py runserver 0.0.0.0:8000

###### nba_web_scraper
- Scrapes game logs from stats.nba.com to later be input into dataAverager.py then eventually to neural network.
                - Formats all data into .csv files which are found in teamGameLogs
                - Used to have extra functionality, but removed any code that wasn't being used in the current version of the project
###### dataAverager.py
- Averages totals of games played up until the given data
- Reformats data to later be input into the neural network.
- Data Format:
  - game
    - Team1 stats before game (array of 20 integer stats)
    - Team2 stats before game (array of 20 integer stats)
    - Winner of game is team 1 (boolean)
###### predictor.py
- Defines the structure of the neural net, and trains it based on data from dataAverager.py
- Final Structure:
  - 1 input layer (flattener)
  - 40 Learning layers activation function relu
  - 2 output layers (outputs being winner of game)
- Training:
  - We trained many neural nets using this file the one we used for the API was trained using
    - 1400 training games
    - 70 test games
    - 1000 epochs (times iterated over training games)
    - Adam Optimizer
  - And achieved an accuracy of 57.4%
- Saves Neural Networks to be used later by the API
###### views.py
- Uses saved neural net in /myModels to predict on saved games in matchups.npy and then expose these predictions through an API listening on port 8000
- API Endpoints:
  - /gamepredictions

# Frontend
![site image](/bnan.PNG)
###### How to run
- download node.js: https://nodejs.org/en/download/
- cd Allan-AdamCapstone/FrontEnd/bnann/
- npm install
- npm start
###### Routes
- Handles all of the frontend that is displayed other than the navigation bar (Home & About page)
###### bnann
- Contains all of the files needed to display and run the front end, also that link the frontend to the backend
###### settings
- \Allan-AdamCapstone\FrontEnd\bnann\src\constants.js
  - Make sure api is set to localhost if running locally
