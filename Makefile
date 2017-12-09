init:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run pytest --cov=mentorship --cov=mentorship_profile --pep8 --cov-branch

ci:
	pipenv run pytest --cov=mentorship --cov=mentorship_profile --pep8 --cov-branch --cov-report term --cov-report html

coverage:
	pipenv run coveralls
