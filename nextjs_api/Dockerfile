FROM python:3.9

WORKDIR /app
COPY requirements.txt /app

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
COPY . /app
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
