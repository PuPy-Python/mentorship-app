init:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run pytest
