init:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run pytest --cov=mentorship --pep8

ci:
	pipenv run pytest --pep8 mentorship --cov=mentorship --cov-report term --cov-report html

coverage:
	pipenv run coveralls
