FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_server.py .

ENV FLASK_APP "flask_server.py"
ENV FLASK_ENV "development"

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]