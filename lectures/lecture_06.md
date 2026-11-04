# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 1:** Foundations & Tooling | **Module 02:** Cloud Tools, DevContainers & AI/LLM Tooling | **Lecture 06:** DevContainers & Docker | Wednesday, September 09, 2026 |

---

## Slide 1: DevContainers & Docker
### Reproducible Environments for Data Science
* **Course Context:** CIS 531/731 - Lecture 06 (Module 02)
* **Core Topic:** Reproducible environments and containerization for data science pipelines
* **Assigned Reading:** Docker Documentation (*Get Started*); PyTorch Docker Hub; NVIDIA Container Toolkit Install Guide
* **Tech Stack:** Docker, VS Code DevContainers, Python 3.11 slim

**Speaker Notes:**
Welcome to Lecture 6. Today we are tackling one of the most persistent bottlenecks in software engineering and data science: environment management. As our pipelines become more complex, involving specific versions of Python, PySpark, CUDA drivers, and system libraries, relying on local manual installations becomes a liability. Today, we transition from relying on our host operating systems to building immutable, containerized development environments using Docker and VS Code DevContainers.

---

## Slide 2: The "It Works On My Machine" Problem
### The Fragility of Local Workspaces
* **Dependency Hell:** Conflicting package versions across different projects (e.g., Project A requires pandas 1.5, Project B requires pandas 2.0).
* **System Drift:** OS-level updates, undocumented terminal commands, and forgotten environment variables that make your setup unique and unreplicable.
* **Collaboration Friction:** Onboarding a new researcher or handing off code to a grader results in hours of troubleshooting installation errors.
* **The Solution:** Isolate the execution environment from the host machine entirely.

**Speaker Notes:**
We have all said it: "It works on my machine." But in research software engineering, if it only works on your machine, it doesn't work. When you publish a paper or hand a project to a grader, they need to be able to run your code immediately. Python virtual environments (`venv`, `conda`) solve part of this by isolating Python packages, but they don't isolate system-level dependencies like C++ compilers or database drivers. We need a heavier layer of isolation.

---

## Slide 3: Virtual Machines vs. Containers
### Two Approaches to Isolation
* **Virtual Machines (VMs):**
  * Hardware-level virtualization.
  * Includes a full Guest Operating System (OS).
  * Heavyweight, slow to boot, allocates fixed RAM/CPU.
  * *Hypervisor:* VMware, VirtualBox.
* **Containers (Docker):**
  * OS-level virtualization.
  * Shares the Host OS kernel; isolates processes, network, and file systems.
  * Lightweight, boots in seconds, dynamic resource usage.
  * *Engine:* Docker Engine, Podman.

**Speaker Notes:**
Historically, to get a clean environment, we spun up Virtual Machines. But VMs are heavy—they emulate a whole motherboard and run a full separate Windows or Linux kernel. Containers take a different approach. Docker isolates the *processes*. A container thinks it is running on a brand-new Linux machine, but it is actually just securely sharing your host computer's operating system kernel. This makes containers incredibly fast and lightweight.

---

## Slide 4: Docker Fundamentals
### Images vs. Containers
* **Docker Image:** The blueprint. A read-only, static snapshot of an environment containing the OS libraries, code, and dependencies.
* **Docker Container:** The running instance. A live, executing process created from the blueprint.
* **Analogy:** An Image is a Class; a Container is an instantiated Object.
* **Immutability:** If a container crashes or is deleted, you simply spin up a new identical one from the Image.

**Speaker Notes:**
You must understand the difference between an Image and a Container. You *build* or *pull* an Image, and you *run* a Container. Because the Image is read-only, it guarantees that every time you start a container from it, it starts from the exact same baseline. You can run five containers from the same image simultaneously, and they will operate completely independently without corrupting the master blueprint.

---

## Slide 5: Anatomy of a Dockerfile
### Infrastructure as Code
* The `Dockerfile` is a plain-text script detailing how to build the Image:
  * **`FROM`**: Defines the base image (e.g., `FROM python:3.11-slim`). Every image starts from another image.
  * **`RUN`**: Executes terminal commands during the build process (e.g., `RUN apt-get update && apt-get install -y git`).
  * **`COPY`**: Transfers files from your host machine into the image (e.g., `COPY requirements.txt /app/`).
  * **`CMD`**: The default command that runs when the container starts (e.g., `CMD ["python", "main.py"]`).

**Speaker Notes:**
This is where "Infrastructure as Code" happens. Instead of writing a README file telling someone to "please install git and python 3.11," you write a Dockerfile. The Docker Engine reads this file from top to bottom and builds the environment automatically. This file gets committed to your git repository right alongside your Python code, explicitly linking the code to the environment it requires to run.

---

## Slide 6: Image Layers & Caching
### Efficient Building
* Every instruction in a Dockerfile (`RUN`, `COPY`) creates a new, distinct layer.
* **Layer Caching:** If a layer hasn't changed, Docker reuses the cached version instead of rebuilding it.
* **Optimization Rule:** Order matters. Put commands that change rarely (like installing OS packages) at the top, and commands that change frequently (like copying your source code) at the bottom.

**Speaker Notes:**
Docker builds are remarkably fast because of the layer cache. However, this means you have to write your Dockerfile strategically. If you copy your active Python script into the image *before* you run `pip install`, Docker will invalidate the cache and reinstall all your pip packages every single time you change one line of code. Always copy your requirements, install them, and *then* copy your volatile source code.

---

## Slide 7: Data Persistence with Volumes
### Ephemeral Environments, Persistent Data
* **The Problem:** By default, containers are ephemeral. If a container stops or is removed, all data written inside it is permanently destroyed.
* **The Solution (Volumes):** Mounting a folder from your host machine into the running container.
* **Bind Mounts:** Maps a specific host path (e.g., `./data/`) to a container path (e.g., `/app/data/`).
* Changes made by the container are saved to your physical hard drive instantly.

**Speaker Notes:**
Containers are meant to be thrown away. You do not want to store your scraped datasets or your trained ML models inside the container's isolated filesystem, or you will lose them when the container dies. We solve this by mounting a Volume. A volume essentially punches a hole through the container's isolation, allowing it to read and write directly to a designated folder on your actual laptop.

---

## Slide 8: Introduction to DevContainers
### The Integrated Development Experience
* **The Concept:** Using a Docker container as your fully-featured development environment, not just for deployment.
* **The Tool:** VS Code "Dev Containers" Extension.
* **How it works:** VS Code boots a Docker container, installs a headless VS Code server *inside* it, and forwards the UI to your local host.
* Your terminal, your extensions, and your Python execution all happen cleanly inside the container.

**Speaker Notes:**
Docker is great for running code, but developing inside a bare terminal container is tedious. Microsoft solved this with DevContainers for VS Code. When you open a DevContainer, VS Code acts as a thin client. You are typing on your laptop, but the execution, debugging, and terminal are actually running completely walled off inside the Docker container. It gives you the UX of local development with the pristine isolation of a container.

---

## Slide 9: Configuring devcontainer.json
### Defining the Workspace
* The `.devcontainer/devcontainer.json` file dictates how VS Code sets up the container:
  * **`image` / `build`:** Specifies which Dockerfile to use.
  * **`customizations.vscode.extensions`:** Automatically installs specific VS Code extensions (like Python, Jupyter, GitHub Copilot) inside the container.
  * **`forwardPorts`:** Maps container ports to your localhost (crucial for viewing Jupyter notebooks or dashboards running inside).
  * **`postCreateCommand`:** Scripts to run after the container starts (e.g., `pip install -r requirements.txt`).

**Speaker Notes:**
Just as the Dockerfile defines the OS environment, the `devcontainer.json` defines the IDE environment. If you want every student in this class to have the exact same Jupyter extension and Python linter installed, you define it in this file. When they clone the repo and open it, VS Code will prompt them to "Reopen in Container," and it will automatically build the environment perfectly, down to the UI extensions.

---

## Slide 10: Multi-Container Environments (Docker Compose)
### A Brief Look at Orchestration
* **The Need:** Real-world data science apps rarely run in a single container. You might need a Python backend, a React frontend, and a PostgreSQL database.
* **Docker Compose:** A tool for defining and running multi-container Docker applications.
* **`docker-compose.yml`:** A YAML file used to configure the application’s services, networks, and volumes.
* **Command:** `docker compose up` spins up the entire microservice architecture at once.

**Speaker Notes:**
We will touch on this more when we deploy our final dashboards, but be aware of Docker Compose. When your project graduates from a simple script to a full application requiring a database and an API, you don't manually start ten different containers. You write a YAML file that defines how all these containers network together, and you launch the entire stack with a single command.
