FROM python:3.9

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

WORKDIR /app/

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
