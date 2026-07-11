## Base Image
# Use a lightweight Python image as the base
FROM python:3.9-slim-bookworm

## Working Directory
# Set the working directory inside the container
WORKDIR /app

## Copy Application Code
# Copy the application code into the container
COPY . /app

## Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

## Expose Port
EXPOSE 8000

## Start Application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# Note: Ensure that the requirements.txt file is present in the same directory as this Dockerfile.
# This Dockerfile sets up a Python environment with the necessary dependencies to run a Flask application.
# The application code should be in the same directory as this Dockerfile.
