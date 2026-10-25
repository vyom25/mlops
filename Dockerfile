FROM python:3.12.12-bookworm

WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "app.py", "run", "--host=0.0.0.0"]