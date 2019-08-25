This api is using existing flask restplus framework for creating api
To run the api one needs to navigate to the app folder and invoke "pip install -r requirements.txt"
Next is to run "python app.py", which will let the user know of the host and port(0.0.0.0:5000)
/upload/ - is for uploading the file , essentially in form of txt or log giving the key value 'file' if using postman
The swagger file can be seen if open directly in browser
Dockerfile is added in the swagger\Dockerfile directory
Docker file can be run "docker build -t mylogparser ./"
To run docker file - "docker run -it -p 5000:5000 mylogparser:latest" the port mapping is 5000
While using browser please navigate to "http://0.0.0.0:5000/" and default>upload>try it>upload file>execute
local_log_parser_image.tar.gz docker image is provided to use in different system

Note: The docker file is using iangolo/meinheld-gunicorn:python3.7-alpine3.8 base image for restplus service of flask and 
is already enabled with multi core processing.