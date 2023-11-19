FROM python:3.10-alpine
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install pymysql
RUN pip install configparser
RUN pip install redis
RUN pip install Flask-Cors
CMD [ "flask", "run", "-h", "0.0.0.0"]