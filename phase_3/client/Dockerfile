FROM python:3.9-slim-buster

# App dependencies
RUN pip install rpyc

# Set the working directory
WORKDIR app

# Install app
COPY client.py .

# Run the Python script when the container starts
CMD ["python", "-u", "client.py"]