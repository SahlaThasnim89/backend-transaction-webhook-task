FROM python:3.11-slim

WORKDIR /app

# Install dependencies for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Make start.sh executable
RUN chmod +x ./start.sh

CMD ["./start.sh"]

