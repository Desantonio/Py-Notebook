# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the specific Python file into the container
COPY python_finance.py .

# Install any required dependencies for the script
RUN pip install yfinance

# Run the Python script when the container starts
CMD ["python", "python_finance.py"]
