# mentorship-app
PuPPy Mentorship Application
[![Build Status](https://travis-ci.org/PuPy-Python/mentorship-app.svg?branch=master)](https://travis-ci.org/PuPy-Python/mentorship-app)
[![Coverage Status](https://coveralls.io/repos/github/PuPy-Python/mentorship-app/badge.svg)](https://coveralls.io/github/PuPy-Python/mentorship-app)


## Basic Pipenv Usage

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

## Testing

To run the tests, run `make test` (no pipenv). This will run `pytest` with
coverage, including all tests written in typical Django style, as well as all
other tests. For info on writing pytest-style Django tests, see
https://pytest-django.readthedocs.io/en/latest/tutorial.html .

## Development

### Depenedencies

Developing on this application requries the follow:

*  Python 3
*  pipenv (https://docs.pipenv.org/)
*  Postgres (https://postgresapp.com/)

### Environment

Required variables:
*  DATABASE_USER
*  DATABASE_URL
*  DATABASE_NAME
*  DATABASE_PASSWORD
*  TEST_DATABASE_NAME
*  EMAIL_HOST_PASSWORD
*  APP_ENV="DEV"