# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /main

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Flask example
EXPOSE 5000
CMD ["python", "main.py"]

