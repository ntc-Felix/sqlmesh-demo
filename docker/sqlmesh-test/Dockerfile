# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the application port
ENV PORT=8000

# Expose the port on which the application will listen
EXPOSE $PORT

# Run the command to start the application
CMD ["sleep","infinity"]