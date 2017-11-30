# mentorship-app
PuPPy Mentorship Application


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

Commit any changes that occur for `Pipfile` and `Pipfile.lock`. For the most
part those should be "the right thing".
