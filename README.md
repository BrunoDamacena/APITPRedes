# API TP Redes

## Prerequisites
- python 3.6+
- pip
- docker
- docker-compose

## Installing
**All commands displayed works on UNIX environment. On Windows, some commands may differ**

Install and configure `virtualenv` with:
```
pip3 install virtualenv
virtualenv venv/
```
Activate the virtual environment with
```
source venv/bin/activate
```
Install all the requirements with:
```
pip3 install -r requirements.txt
```

## Running API
There are two ways to execute the API itself: using python entrypoint (1) or using the Dockerfile (2)

1. Executing app.py
```
python app.py
```
API will be available in `localhost:5000`

2. Using Dockerfile
The Dockerfile implemented use `gunicorn` to deploy the Flask API. Gunicorn is a Python WSGI HTTP Server for UNIX which executes the Flask app handling multiple workers and the communication with the webserver.
- Build image:
```
docker build -t api .
```
- Run container mapping `logs` folder:
```
docker run -v ($pwd)/logs:/app/logs -p 5000:5000 api
```
API will be available in `localhost:5000`

## Deploying
In order to deploy the fully API stack, a `docker-compose.yml` was developed. The stack contains two services: the Flask API with Gunicorn and a `nginx` server. The Nginx server is responsible to make the comunication between the external world and the Gunicorn, proxying the correct requests to the API.
- Building:
```
docker-compose build
```
- Running:
```
docker-compose up -d
```
Nginx server will listen to `localhost:81` and proxy the requests to the Gunicorn service, which is listening to port 5000 (not exposed to external world)
