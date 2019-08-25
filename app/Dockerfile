FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8


RUN pip install flask
RUN pip install flask_restplus
RUN pip install werkzeug


WORKDIR /app
COPY ./app /app


ENTRYPOINT [ "python" ]

CMD [ "app.py" ]