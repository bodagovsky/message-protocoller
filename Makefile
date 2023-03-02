
build:
	docker build -f Dockerfile -t listener .

push:
	docker push listener:latest

greeting:
	echo "hello world"

check:
	echo $(secret)