# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]

