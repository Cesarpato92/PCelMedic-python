
# Imagen base de Python 3.10
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias para Tkinter en el contenedor
RUN apt-get update && apt-get install -y \
    tk \
    libx11-6 \
    xdg-utils \ 
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la estructura del proyecto
COPY GUI/ ./GUI/
COPY Logica/ ./Logica/
COPY DAO/ ./DAO/
COPY Modelo/ ./Modelo/
COPY Utilidades/ ./Utilidades/
COPY Config/ ./Config/
COPY .configAdmin .
COPY main.py .

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]