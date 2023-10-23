# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install application dependencies (if you have a requirements.txt file)
RUN pip install -r requirements.txt

# Expose the port your application will run on
EXPOSE 

# Define the command to run when the container starts
CMD ["python", "app.py"]
