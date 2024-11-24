FROM python:3.10.15-slim-bullseye

WORKDIR /appd

COPY requirements.txt requirements.txt
COPY templates templates

RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
