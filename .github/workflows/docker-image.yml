# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire application directory into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which your Flask app runs
EXPOSE 5000

# Define environment variable to tell Flask where to find the app
ENV FLASK_APP=app.py

# Run the application
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0
