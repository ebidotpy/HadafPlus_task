# Use official Python image as base
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -L https://ollama.com/install.sh | sh

# Create and set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Download models (optional - can be done at runtime)
RUN ollama pull llama3
RUN ollama pull persian-llama  # If using a Persian-tuned version

# Expose ports
EXPOSE 8000  
EXPOSE 11434  


# Command to run the application
CMD ["sh", "-c", "ollama serve & uvicorn api.server:app --host 0.0.0.0 --port 8000"]