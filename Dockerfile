FROM python:3.9.1

ADD main.py .

RUN pip install json sys csv Fernet

CMD [ "python", "./main.py" ]