# Development

How to setup the application and instructions for common development tasks such as testing.

## Setup
How to setup this application for development.

### Depenedencies
Developing on this application requires the following:

*  Python 3
*  pipenv (https://docs.pipenv.org/)
*  Postgres (https://postgresapp.com/)
*  make (https://www.gnu.org/software/make/)

#### Basic Pipenv Usage

Make sure you have pipenv. A large number of pipenv installation options
are covered in the documentation at https://docs.pipenv.org .

After you clone the project, run `pipenv install --dev`. This will install
all the project dependencies in a virtualenv that pipenv manages. To run
commands inside the virtualenv, use `pipenv run COMMAND [ARGS]`. For example,
`pipenv run python manage.py help`. Alternatively, you can open a shell inside
the virtualenv with `pipenv shell`, and then run commands as normal. For
example, you could run `python manage.py help` inside `pipenv shell`.


While developing, if you need to install a new package, run
`pipenv install packagename`. If the package is not needed for deployment, run
`pipenv install --dev packagename`. To uninstall a package, replace `install`
with `uninstall`.

Before updating your pull request, run `pipenv lock` if you have installed
any new packages. It is safe to run this if you have not installed anything
(no changes will be made), so if you are not sure, go ahead and run it.

Commit any changes that occur for `Pipfile` and `Pipfile.lock`. For the most
part those should be "the right thing".

### Getting Started
Once all dependencies are installed and the repository is cloned, perform the following steps:

    1. Create local databases for the application and for testing (assuming postgres cli is installed):
        `createdb mentorship`
        `createdb test_mentorship`

    2. Create a `.env` file in the project root and populate it with the following variables:
        *  DATABASE_USER                # Your computer username by default
        *  DATABASE_URL=127.0.0.1
        *  DATABASE_NAME                # e.g. 'puppy_mentors'
        *  DATABASE_PASSWORD            # If you set up a password for your local DB
        *  TEST_DATABASE_NAME           # e.g. 'test_puppy_mentors'
        *  EMAIL_HOST_PASSWORD          # Ask a Contributor
        *  APP_ENV="DEV"
        *  DEBUG="True"
        *  SECRET_KEY                   # Something secret.

    3. Install the application using make command:
        `make init`

    4. Start the application using make command:
        `make run`

### Basic Commands
This project uses a Makefile to abstract most of the common commands for development.  Examples below:

`make test` (runs pytest using pipenv)

`make run` (starts the application)

`make makemigrations` (makes database migrations, e.g. `./manage.py makemigrations`)

`make migrate` (migrates the database changes, e.g. `./manage.py migrate`)

## Testing

To run the tests, run `make test` (no pipenv). This will run `pytest` with
coverage, including all tests written in typical Django style, as well as all
other tests. For info on writing pytest-style Django tests, see
https://pytest-django.readthedocs.io/en/latest/tutorial.html .

When adding a new Django "Application" in order to run the tests from that application, it must be added to the command like so: `--cov=mentorship_newapp`

## Resources
This application uses React, Django, and Django Rest Framework.  Their documentation is below:

### React
Documentation: https://reactjs.org/docs/getting-started.html

### Django
Documentation: https://docs.djangoproject.com/en/1.11/

### Django Rest Framework
Documentation: http://www.django-rest-framework.org/

### React and DRF App on Heroku:
Tutorial for deploying a React / Django app on heroku
https://medium.com/@nicholaskajoh/deploy-your-react-django-app-on-heroku-335af9dab8a3