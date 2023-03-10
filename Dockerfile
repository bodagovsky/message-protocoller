FROM python:3.10

WORKDIR /listener

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

