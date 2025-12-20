FROM python:3.11-slim

WORKDIR /app

# Copy dependencies from root
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

CMD ["./start.sh"]




