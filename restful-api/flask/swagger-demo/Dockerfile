FROM python:3

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP "main.py"
ENV FLASK_ENV "development"

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]