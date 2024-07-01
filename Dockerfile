# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (pytube)
RUN pip install --no-cache-dir pytube

# Run the Python script when the container launches
ENTRYPOINT ["python", "app.py"]