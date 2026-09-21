# ==============================================================================
# CIS 531/731: Minimal DevContainer Dockerfile (MP2)
# ==============================================================================

# 1. Switch to Debian Archive mirrors and bypass expiration checks
FROM python:3.10-slim-bullseye

RUN echo "deb http://archive.debian.org/debian/ bullseye main" > /etc/apt/sources.list && \
    echo "Acquire::Check-Valid-Until \"false\";" > /etc/apt/apt.conf.d/99no-check-valid-until

# 2. Install System Dependencies (Java for PySpark, FFmpeg for Whisper)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-11-jre-headless \
    ffmpeg \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# 3. Configure Environment Variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PIP_NO_CACHE_DIR=1

# 4. Install Python Dependencies (Strict Pinned Versions per MP2 Manifest)
RUN pip install --upgrade pip && \
    pip install \
    pyspark==3.5.1 \
    torch==2.2.1 \
    transformers==4.38.2 \
    openai-whisper==20231117 \
    mlflow==2.11.1 \
    faiss-cpu==1.8.0

# 5. Create Non-Root User (Required for standard DevContainer permissions)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace