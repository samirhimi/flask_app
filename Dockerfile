# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files into the container

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py /app/
COPY templates /app/templates/
COPY static /app/static/

# Install Flask and any other dependencies
RUN pip install flask

# Expose the Flask app's port
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]
