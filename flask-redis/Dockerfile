# Start with Python already installed in a minimal Linux environment.
# Flask and the Redis client still need to be installed separately.
FROM python:3.13-slim

# Set the working directory inside the image, creating it if needed.
# Relative destinations and subsequent commands use this directory.
WORKDIR /app

# Copy the dependency list from the build context into /app.
COPY requirements.txt .

# Install dependencies during the image build.
# Copying app.py afterward lets Docker reuse this step when only code changes.
RUN pip install -r requirements.txt

# Add the application code to /app inside the image.
COPY app.py .

# Document Flask's internal listening port.
# This does not publish a port to your Mac; Compose controls port publishing.
EXPOSE 5000

# Default startup command when a container runs from this image.
# Execute app.py, whose app.run(...) call starts Flask's server.
CMD ["python", "app.py"]