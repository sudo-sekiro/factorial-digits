FROM python:3

ADD factorial-digits.py .

RUN pip install numpy

ENTRYPOINT [ "python", "./factorial-digits.py" ]