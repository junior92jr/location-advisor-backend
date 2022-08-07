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


# Location Advisor Backend

## Table of contents

1. [Regular Installation](#markdown-header-regular-installation)
2. [Running the project](#markdown-header-running-the-project)
3. [Build Documentation](#markdown-header-build-documentation)
4. [Installation with Docker](#markdown-header-dockerization)

`

## Configure the project
### Create a virtualenv

```
$ python3 -m venv location_advisor
```

This command will create a new folder with the name `location_advisor`

### Clone the project

First verify your SSH Keys on github configuration
then if you dont have a key that points to your computer follow this tutorial:

* https://docs.github.com/de/developers/overview/managing-deploy-keys

```
$ git clone git@github.com:junior92jr/location-advisor-backend.git
```

### Activate your enviroment
Inside the `location_advisor` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(location_advisor) $
```

### Install requirements
```
(location_advisor)$ cd location_advisor_backend

(location_advisor)$ pip install -r requirements.txt
```

### Setting up environment variables for project

For environment variables configuration, you will need a .env file in the parent directory of the current folder.

```
(location_advisor) $ touch ../.env
```

../.env example

```
DEBUG=True

SECRET_KEY="secret_key_for_django_application"

FOURSQUARE_API_KEY="external_service_api_key"
```


# Running the project
## Run the project

Once you have everything ok, you can run the project.

```
(location_advisor) $ ./manage.py check

(location_advisor) $ ./manage.py migrate

(location_advisor) $ ./manage.py runserver
```

## Run tests

Coverage is configured for the project for running tests and measuring in Scrutinizer

```
(location_advisor) $ coverage run --source="." manage.py test --settings=location_advisor.test_settings --verbosity=2
```

Once ran, if you want to see fast the results you can run

```
(location_advisor) $ coverage report
```

or you can run 

```
(location_advisor) $ coverage html
```

and an HTML view of your test coverage will be generated in htmlcov/index.html

# Build Documentation

Sphinx is configured to build a user friendly site for code documentation.

To build this files run

```
(location_advisor) $ cd docs
(location_advisor) $ make html
```

They will be build in docs/build/html/ with index.html as the main page.
It can also be accessed from the admin site in the top navigation.
