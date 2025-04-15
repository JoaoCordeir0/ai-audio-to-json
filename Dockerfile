FROM python:3.11-slim

USER root

RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    curl \
    tesseract-ocr \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Diretório da aplicação
WORKDIR /app

# Cria a pasta tmp
RUN mkdir -p /app/tmp

# Cria e ativa um ambiente virtual
RUN python3.11 -m venv /venv

# Define o ambiente virtual como o padrão
ENV PATH="/venv/bin:$PATH"

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python no ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código-fonte para o diretório de trabalho
COPY . .

# Expoẽ a porta 8000
EXPOSE 8000

# Defina o comando padrão para executar o script Python
CMD ["python", "main.py"]

