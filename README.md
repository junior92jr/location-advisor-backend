# foursquare-client

This is the challenge required for foursquare API:

## Requeriments
1) Linux
2) Pip
3) Virtualenv
4) Python3

## Instructions
1) mkdir challenge_dir
2) virtualenv -p python3 challenge_dir
3) cd challenge_dir/
4) source bin/activate
5) git clone https://github.com/junior92jr/foursquare-client.git
6) cd foursquare-client/
7) pip install -r requeriments.txt
8) python manage.py migrate
9) python manage.py runserver

## Testing
You nee to run the project in your localhost like this:
  - http://127.0.0.1:8000
After that you need to access to the endpoint:
  - http://127.0.0.1:8000/api/recomendations/
You can try some parameters in the GET method:
  - http://127.0.0.1:8000/api/recomendations/?lat=-16.39889;lng=-71.535
  - http://127.0.0.1:8000/api/recomendations/?lat=-16.39889;lng=-71.535;category=outdoors
  
Category parameters could be:
1) food
2) drinks 
3) coffee 
4) shops
5) arts
6) outdoors
7) sights
8) trending
9) nextVenues
10)topPicks
As valid options
