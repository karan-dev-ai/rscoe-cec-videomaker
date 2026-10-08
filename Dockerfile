FROM python:3.11-slim

# Install system ffmpeg, fonts, and essential tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    fonts-dejavu-core \
    fontconfig \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Hugging Face Spaces runs as user ID 1000
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONUNBUFFERED=1

WORKDIR $HOME/app

# Install dependencies first for fast layer caching
COPY --chown=user:user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy application files
COPY --chown=user:user . .

# Ensure working directories exist with proper write permissions
RUN mkdir -p uploads outputs assets/music assets/logo assets/fonts

EXPOSE 8000
EXPOSE 10000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]

