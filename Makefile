
build:
	docker build -f Dockerfile -t listener .

push:
	docker push listener:latest

greeting:
	echo "hello world"

check:
	if [ -z $(secret)] ; then echo 'secret is empty'; else echo 'successfully extracted non-empty secret'; fi