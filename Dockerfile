# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /backend

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ./backend ./backend

# Run FastAPI using uvicorn
CMD ["uvicorn", "backend.v1.app.api.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
