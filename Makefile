DOCKERFILE := Dockerfile 
APP_NAME := flaskdash
APP_PORT := 7777

stop:
	docker stop ${APP_NAME} && docker rm -f ${APP_NAME} || true

build: stop
	docker build -f ${DOCKERFILE} -t ${APP_NAME}:latest .

run: stop build 
	docker run -d -p ${APP_PORT}:8080 --name ${APP_NAME} ${APP_NAME}:latest gunicorn -b 0.0.0.0:8080 --reload 'main:app'

logs:
	docker logs ${APP_NAME} --tail 100 -f