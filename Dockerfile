FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8
#it is using gunicorn base image which has multi core processing configured already

#installing dependencies
RUN pip install flask
RUN pip install flask_restplus
RUN pip install werkzeug



COPY ./app /app

WORKDIR /app
ENTRYPOINT [ "python" ]

#port exposed for container
EXPOSE 5000


CMD [ "app.py" ]