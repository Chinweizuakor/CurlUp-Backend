# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . /workspace

# Install dependencies
RUN pip install --no-cache-dir -r /workspace/backend/requirements.txt

# Run FastAPI using uvicorn
CMD ["uvicorn", "backend.v1.app.server.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
