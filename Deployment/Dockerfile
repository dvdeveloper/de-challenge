#Dockerfile
FROM python:3.8-slim

ADD main.py /
COPY data data/
COPY output output/

RUN pip install pandas

CMD [ "python", "./main.py" ]