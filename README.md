# Kubernetes-Based AI API Deployment

A lightweight AI prediction API built using FastAPI and structured for containerized deployment workflows using Docker and Kubernetes concepts.

This project was created to explore cloud-native application deployment, API development, containerization, and beginner-level Kubernetes orchestration workflows.

---

# Project Overview

The project provides a simple AI prediction API that accepts JSON input and returns prediction results through REST endpoints.

The application was structured using:
- FastAPI for backend API development
- Docker for containerization
- Kubernetes YAML configurations for deployment orchestration
- Minikube and kubectl for local Kubernetes learning and deployment practice

---

# Features

- FastAPI-based REST API
- Lightweight prediction endpoint
- Docker containerization workflow
- Kubernetes Deployment configuration
- Kubernetes Service exposure
- Pod scaling and orchestration concepts
- Local Kubernetes practice using Minikube

---

# Tech Stack

- Python
- FastAPI
- Docker
- Kubernetes
- Minikube
- kubectl

---

# Project Structure

```bash
AI_API_Kubernetes_Deployment/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── README.md
└── screenshots/
```

---

# API Endpoints

## Home Endpoint

```http
GET /
```

### Example Response

```json
{
  "message": "AI API Running Successfully"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

### Example Input

```json
{
  "value": 70
}
```

### Example Output

```json
{
  "prediction": "High"
}
```

---

# Kubernetes Concepts Explored

- Deployments
- Services
- Pod Management
- Containerized Workloads
- Service Exposure
- Scaling Concepts
- YAML Configuration
- kubectl Commands
- Minikube-based Local Cluster Practice

---

# Screenshots

## FastAPI Swagger UI

Add screenshot inside:
screenshots/swagger-ui.png

## API Prediction Example

Add screenshot inside:
screenshots/predict-api.png

## Terminal Execution

Add screenshot inside:
screenshots/terminal-run.png

---

# Learning Outcome

Through this project, I explored:
- API deployment workflows
- Docker-based application packaging
- Kubernetes configuration structure
- Basic container orchestration concepts
- Cloud-native development practices

This project helped me better understand how AI applications can be prepared for scalable deployment environments.

---

# Future Improvements

- Add database integration
- Add authentication
- Deploy on cloud platform
- Add CI/CD workflow
- Add monitoring and logging
- Deploy using managed Kubernetes services

---

# Author

Harshal Badgujar

GitHub:
https://github.com/BadgujarHarshal