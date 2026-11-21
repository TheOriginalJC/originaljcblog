# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install the hash-locked dependencies
RUN python -m pip install --no-cache-dir --require-hashes -r requirements.txt

# Default command to build site
 CMD ["python", "build_blog.py"]