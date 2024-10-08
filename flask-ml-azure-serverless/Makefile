# setup:
	# python3 -m venv env_azure
	# source env_azure/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203,W0702 app.py

docker-build:
	docker build -t boston-house-app .

docker-run:
	docker run -p 5000:5000 boston-house-app

docker-debug:
	#to debug inside the container
	docker run -d -p 5000:5000 --name boston-container boston-house-app
	docker exec -it boston-container bash

docker-clean:
	#remove all images locally
	if [ -n "$$(docker images -aq)" ]; then \
		docker rmi -f $$(docker images -aq); \
	fi

all: install lint test
