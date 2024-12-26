# Use a Python 3.8 base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Flask and other required libraries
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the working directory
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
