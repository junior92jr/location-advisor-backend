# Location Advisor Backend

This backend project is a Rest Api that provides touristic information for a Frontend project.
Main source of the information comes from Foursquare:

* https://foursquare.com/

It provides recommendations for touristic destinations based on your current location.

This API should provide dynamic information that will be displayed in a frontend project.


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

Note: Coverage stills missing but tests are running with test.py django command.

# Build Documentation

Sphinx is configured to build a user friendly site for code documentation.

To build this files run

```
(location_advisor) $ cd docs
(location_advisor) $ make html
```

They will be build in docs/build/html/ with index.html as the main page.
It can also be accessed from the admin site in the top navigation.

Note: Docstrings ready for Documentation but adding the library is missing.
