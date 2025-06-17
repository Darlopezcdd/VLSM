
FROM python:3.12-slim
RUN apt-get update && apt-get install -y \
    libgobject-2.0-0 \
    libcairo2 \
    libpango-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libjpeg8 \
    libgif7 \
    libwebkit2gtk-4.0-37 \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
