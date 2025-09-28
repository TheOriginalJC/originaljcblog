# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies (markdown library)
RUN pip install --no-cache-dir markdown pyyaml

# Default command to build site
CMD ["python", "build.py"]