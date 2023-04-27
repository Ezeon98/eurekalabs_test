# Imagen base de Python
FROM python:3.9-slim-buster

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copiar los requerimientos e instalar las dependencias
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código de la aplicación
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app


# Iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]