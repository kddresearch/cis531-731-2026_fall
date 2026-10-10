# ==============================================================================
# CIS 531/731: Minimal DevContainer Dockerfile (MP2)
# ==============================================================================
FROM python:3.10-slim-bookworm

# 1. Install System Dependencies (Java for PySpark, FFmpeg for Whisper)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-17-jre-headless \
    ffmpeg \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# 2. Configure Environment Variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PIP_NO_CACHE_DIR=1

# 3. Install Python Dependencies (Strict Pinned Versions per MP2 Manifest)
#    Fix: openai-whisper==20231117 needs pkg_resources, which setuptools>=81 removed.
#    Pin setuptools and build whisper without pip's isolated (latest-setuptools) build env.
RUN pip install --upgrade pip && \
    pip install "setuptools<81" wheel && \
    pip install \
    pyspark==3.5.1 \
    torch==2.2.1 \
    transformers==4.38.2 \
    mlflow==2.11.1 \
    faiss-cpu==1.8.0 && \
    pip install --no-build-isolation openai-whisper==20231117

# 4. Create Non-Root User (Required for standard DevContainer permissions)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace
#I made changse to python and java versions as I couldnt get it to
#run otherwise and that is what I have installed and have been using
#please message me if that was not approperate for the class