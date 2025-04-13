# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy dependencies to requirements to do easier the future instalations

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt # Instaling de dependencies

# Copy the entire project
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
