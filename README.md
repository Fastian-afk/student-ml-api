# student-ml-api

> **Production-oriented FastAPI inference service with professional CI/CD, Docker, semantic versioning, and automated GHCR releases.**

[![CI](https://github.com/Fastian-afk/student-ml-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Fastian-afk/student-ml-api/actions/workflows/ci.yml)
[![Release](https://github.com/Fastian-afk/student-ml-api/actions/workflows/release.yml/badge.svg)](https://github.com/Fastian-afk/student-ml-api/actions/workflows/release.yml)

## Overview

`student-ml-api` is a lightweight REST API built with **FastAPI** and designed as a practical MLOps deployment workflow.

The project demonstrates an end-to-end software delivery pipeline:

**Feature Branch → Pull Request → CI Validation → Merge → Semantic Version Tag → Docker Build → GHCR Publication**

The application provides a health endpoint with application/model metadata and a deterministic prediction endpoint for inference testing.

## Features

* ⚡ **FastAPI** REST API
* 🩺 Health monitoring through `/health`
* 🤖 Deterministic prediction through `/predict`
* 🧪 Automated unit testing with `pytest`
* 🐳 Production-oriented Docker containerization
* 🔄 GitHub Actions CI for pull requests
* 📦 Automated Docker image publishing to **GitHub Container Registry**
* 🏷️ Semantic versioning with Git tags
* 🔎 Commit-specific Docker image tags for traceability
* 🧾 OCI image metadata for release provenance
* 🔐 Protected `main` branch with required CI checks
* ♻️ Versioned releases supporting reproducible deployment and rollback

## API Endpoints

### `GET /health`

Returns application and model health information.

Example response:

```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

### `POST /predict`

Accepts a numeric input and returns a deterministic prediction.

Request:

```json
{
  "value": 10
}
```

Response:

```json
{
  "input": 10,
  "prediction": 20
}
```

Invalid or missing input is rejected through FastAPI/Pydantic validation.

## Project Structure

```text
student-ml-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── VERSION
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        ├── ci.yml
        └── release.yml
```

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/Fastian-afk/student-ml-api.git
cd student-ml-api
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run tests

```bash
python -m pytest
```

### 5. Start the API

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## Docker

Build the image locally:

```bash
docker build -t student-ml-api:1.1.0 .
```

Run the container:

```bash
docker run -d --name student-ml-api -p 5000:8000 student-ml-api:1.1.0
```

Test the health endpoint:

```text
http://localhost:5000/health
```

View container logs:

```bash
docker logs student-ml-api
```

Inspect the container:

```bash
docker inspect student-ml-api
```

## Continuous Integration

Every pull request targeting `main` runs automated validation through GitHub Actions.

The CI pipeline:

1. Checks out the source code.
2. Sets up Python 3.12.
3. Installs project dependencies.
4. Runs the complete test suite.
5. Builds the Docker image.

A pull request cannot be merged into the protected `main` branch unless the required CI checks pass.

## Release Pipeline

Production Docker images are published automatically when a semantic Git tag is pushed.

Example:

```bash
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0
```

The release workflow automatically:

* Runs the test suite.
* Derives the release version from the Git tag.
* Authenticates securely to GHCR using `GITHUB_TOKEN`.
* Builds the Docker image.
* Publishes the semantic version tag.
* Updates the `latest` tag.
* Publishes a short commit-SHA tag.
* Adds OCI image metadata for traceability.

### Published Image

```text
ghcr.io/fastian-afk/student-ml-api:1.1.0
ghcr.io/fastian-afk/student-ml-api:latest
```

A commit-specific image is also published for immutable traceability.

## Versioning

The project uses **Semantic Versioning**:

```text
v1.0.0
v1.1.0
```

The `VERSION` file stores the application version used by the API.

This creates a traceable relationship between:

```text
Pull Request
    ↓
Merge Commit
    ↓
Git Tag
    ↓
Docker Image Tag
    ↓
Docker Image Digest
```

## MLOps Workflow

```text
Developer
   │
   ▼
Feature Branch
   │
   ▼
Commit + Push
   │
   ▼
Pull Request
   │
   ▼
GitHub Actions CI
 ┌───────────────┐
 │ Unit Tests    │
 │ Docker Build  │
 └───────────────┘
   │
   ▼
Review + Merge
   │
   ▼
Semantic Git Tag
   │
   ▼
Release Workflow
   │
   ├── Tests
   ├── Build
   ├── Metadata
   └── Publish
   │
   ▼
GitHub Container Registry
```

## Technology Stack

| Component          | Technology                |
| ------------------ | ------------------------- |
| API Framework      | FastAPI                   |
| Runtime            | Python 3.12               |
| ASGI Server        | Uvicorn                   |
| Validation         | Pydantic                  |
| Testing            | Pytest                    |
| Containerization   | Docker                    |
| CI/CD              | GitHub Actions            |
| Container Registry | GitHub Container Registry |
| Version Control    | Git + GitHub              |
| Versioning         | Semantic Versioning       |

## Repository

**GitHub:**
[https://github.com/Fastian-afk/student-ml-api](https://github.com/Fastian-afk/student-ml-api)

**Container Registry:**
`ghcr.io/fastian-afk/student-ml-api`

---

### Current Release

**Application Version:** `1.1.0`
**Model Version:** `model-1`

Built with a focus on **reproducibility, traceability, automated validation, and deployment consistency**.
