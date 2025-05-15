# Use a base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /eventify

# Install system dependencies
RUN apt-get update && apt-get install -y curl && apt-get clean

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy pyproject.toml and optional poetry.lock/pip.lock first for layer caching
COPY pyproject.toml ./

# Install dependencies using uv
RUN uv pip install --system --no-deps --requirement <(uv pip compile pyproject.toml)

# Now copy rest of the app
COPY . .

# Expose port (optional)
EXPOSE 8000

# Run your app (change as needed)
CMD ["python", "asgi.py"]
