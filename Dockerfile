# Production Dockerfile for OpenEnv Submission
# Environment: Python 3.11-slim
FROM python:3.11-slim

# Set non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install critical system tools
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency manifest
COPY requirements.txt .

# Install dependencies with no cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy complete modular codebase
COPY . .

# Expose required ports (HF Spaces default: 7860)
EXPOSE 7860

# Metadata Labels
LABEL org.openenv.name="customer-service-agents-openenv"
LABEL org.openenv.task="CSA-001"

# The Space must serve the environment to respond to /reset pings
# We use uvicorn to serve the OpenEnv FastAPI interface
CMD ["python", "-m", "openenv_core.server", "--env-entrypoint", "customer_service_env:CustomerServiceEnv", "--host", "0.0.0.0", "--port", "7860"]
