#python image:python:3.8
#FROM python:alpine3.16
#FROM krnpatel/flask-app:python3.11

FROM python:3.9.18-alpine3.18

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 8081

# run the command
CMD ["python", "app.py"]