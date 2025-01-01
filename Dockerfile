FROM python:3.10-slim

WORKDIR /app

# Copy only the requirements file first to leverage Docker's caching mechanism
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application code (excluding tests and unnecessary files via .dockerignore)
COPY app /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
