
docker: auth build push

auth:
	docker login -p $(docker_pass) -u $(docker_user)

build:
	docker build -f Dockerfile -t bodagovsky/message-protocoller .

push:
	docker push bodagovsky/message-protocoller:latest

