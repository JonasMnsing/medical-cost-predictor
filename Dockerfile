# Use Python 3.11 since that matches your local pipenv environment
FROM python:3.11-slim

# Install pipenv
RUN pip install pipenv

# Create a working directory inside the container
WORKDIR /app

# Copy the dependency files
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies strictly into the container's system 
RUN pipenv install --system --deploy

# Copy your script and the trained model
COPY ["predict.py", "model.bin", "./"]

# Expose the port your app runs on
EXPOSE 9696

# Start the production server
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]