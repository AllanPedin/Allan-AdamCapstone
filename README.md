# Allan-AdamCapstone
Neural Net that analyzes and predicts the winner of basketball games.

# Backend
nba_web_scraper - Scrapes game logs from stats.nba.com to later be input into dataAverager.py then eventually to neural network.
                - Formats all data into .csv files which are found in teamGameLogs
                - Used to have extra functionality, but removed any code that wasn't being used in the current version of the project
dataAverager.py - Averages totals of games played up until the given data
                - Reformats data to later be input into the neural network.
predictor.py    - Neural network that analyzes data given through dataAverager.py and then makes predictions on which team will win

# Frontend
Routes          - Handles all of the frontend that is displayed other than the navigation bar (Home & About page)
bnann           - Contains all of the files needed to display and run the front end, also that link the frontend to the backend
