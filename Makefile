CONTAINER_NAME := gl-flask-app
IMAGE_NAME := gl-flask-image
DOCKER_LOGIN := rudychuk

build:
	docker build -t $(IMAGE_NAME):latest .

run:
	docker run -d --name $(CONTAINER_NAME) -p 8080:8080 $(IMAGE_NAME):latest

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rm $(CONTAINER_NAME)

clean-image:
	docker rmi $(IMAGE_NAME):latest

push:
	docker push $(DOCKER_LOGIN)/$(IMAGE_NAME):latest

prospector:
	prospector --profile=config/prospector.yaml

test:
	python -m unittest tests/test.py 

