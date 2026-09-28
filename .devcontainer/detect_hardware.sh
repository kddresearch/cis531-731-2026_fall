#!/usr/bin/env bash
set -euo pipefail

DOCKERFILE=docker/Dockerfile

if command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi >/dev/null 2>&1; then
  HARDWARE=gpu
  echo "[detect_hardware] GPU detected -> building GPU base image (nvidia/cuda)"
else
  HARDWARE=cpu
  echo "[detect_hardware] No GPU detected -> building CPU base image (python:3.10-slim-bullseye)"
fi

# NOTE: devcontainer.json's build.args + ${localEnv:HARDWARE} cannot see
# variables exported here, since this script runs as a child process whose
# environment doesn't propagate back to the devcontainer CLI's own build-arg
# resolution. Instead, rewrite the Dockerfile's ARG default directly.
sed -i.bak "s/^ARG HARDWARE=.*/ARG HARDWARE=${HARDWARE}/" "$DOCKERFILE"
rm -f "${DOCKERFILE}.bak"

mkdir -p .devcontainer
echo "HARDWARE=${HARDWARE}" > .devcontainer/.env