init:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run pytest --cov=mentorship --cov=mentorship_profile --cov=mentorship_pairing --cov=mentorship_api --pep8 --cov-branch --cov-report term-missing

ci:
	pipenv run pytest --pep8 --cov=mentorship --cov=mentorship_profile --cov=mentorship_pairing --cov=mentorship_api --cov-report term --cov-report html --cov-branch

coverage:
	pipenv run coveralls

run:
	pipenv run ./manage.py runserver

makemigrations:
	pipenv run ./manage.py makemigrations

migrate:
	pipenv run ./manage.py migrate

# run commands after building image and mounting /app volume
docker:
	pip install pipenv
	pipenv install --dev --ignore-pipfile
	pipenv run ./manage.py migrate
	yarn install
	yarn start &
	pipenv run ./manage.py runserver 0.0.0.0:8000
