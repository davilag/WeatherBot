FROM python:3

ADD start.py /

ADD . /weather-bot

WORKDIR /weather-bot

RUN pip3 install -r requirements.txt

CMD [ "python3", "start.py" ]
