
SHELL := /bin/bash

docker-build:
	docker build -t my-php-app .

docker-run-local: # docker-build
	docker run -it -p 8080:80 my-php-app

docker-run-bash: # docker-build
	docker run -it -p 8080:80 my-php-app bash

build-and-run:docker-build docker-run-local
