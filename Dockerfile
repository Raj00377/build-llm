
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies
RUN uv lock && uv sync --frozen

# Copy application
COPY . .

# Run Python application
CMD ["uv", "run", "python", "main.py"]