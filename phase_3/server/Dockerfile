FROM python:3.9-slim-buster

# App dependencies
RUN pip install rpyc requests

# Set the working directory
WORKDIR app

# Install app
COPY server.py .
COPY api.py .
COPY healthcheck.py .

# Run the Python script when the container starts
CMD ["python", "-u", "server.py"]
