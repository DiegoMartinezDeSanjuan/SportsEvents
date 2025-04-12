# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Primero copiamos las dependencias

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  #  Luego las instalamos

# Finalmente, copiamos el resto del proyecto
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
