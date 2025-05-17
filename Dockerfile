# Use the official PyTorch image https://pypi.org/project/torch/2.6.0/#docker-image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY *.py .
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api:app"]