FROM python:3.9-slim-buster

# App dependencies
RUN pip install rpyc requests

# Set the working directory
WORKDIR app

# Install app
COPY server.py .
COPY api.py .

# Expose port
EXPOSE 18861

# Run the Python script when the container starts
CMD ["python", "-u", "server.py"]
