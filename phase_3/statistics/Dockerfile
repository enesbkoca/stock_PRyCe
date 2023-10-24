FROM python:3.9-slim-buster

# App dependencies
RUN pip install docker

# Set the working directory
WORKDIR app

# Install app
COPY statistics.py .

# Run the Python script when the container starts
CMD ["python", "-u", "statistics.py"]
