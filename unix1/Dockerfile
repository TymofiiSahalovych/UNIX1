FROM python:3.11-slim

WORKDIR /

RUN pip install Flask

COPY . .

EXPOSE 8800

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8800"]