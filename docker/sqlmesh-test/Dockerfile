# Use an official Python runtime as a parent image
FROM python:3.10

RUN apt-get update && apt-get install -y libpq-dev

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install psycopg2 for PostgreSQL support
RUN pip install psycopg2-binary==2.9.1

# Set the working directory to /app
#WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Set the environment variable for the application port
ENV PORT=8000

# Expose the port on which the application will listen
EXPOSE $PORT

# Run the command to start the application
CMD ["python","app/main.py"]