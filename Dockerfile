FROM python:3.7-alpine
RUN apk update
WORKDIR /converter
ADD . /converter
RUN pip install -r requirements.txt
CMD ["python3","app.py"]