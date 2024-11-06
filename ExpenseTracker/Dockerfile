# Use the official Python image from the Docker Hub
FROM python:3.9-slim AS backend

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code
COPY . /app/

# Use the official Node.js image to build the frontend assets
FROM node:14 AS frontend

# Set the working directory
WORKDIR /app

# Copy the frontend code
COPY static /app/static
COPY templates /app/templates

# Install Node.js dependencies if any (optional)
# RUN npm install

# Build the frontend assets if needed (optional)
# RUN npm run build

# Use the official Python image from the Docker Hub for the final stage
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the backend dependencies and code from the backend stage
COPY --from=backend /app /app

# Copy the built frontend assets from the frontend stage
COPY --from=frontend /app/static /app/static
COPY --from=frontend /app/templates /app/templates

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]