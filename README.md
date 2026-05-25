# Kubernetes-Based AI API Deployment

This project demonstrates deployment of a lightweight AI prediction API using FastAPI, Docker, and Kubernetes concepts.

## Features
- FastAPI-based AI API
- Docker containerization
- Kubernetes Deployment and Service configuration
- Pod scaling concepts
- Container orchestration basics

## Tech Stack
- Python
- FastAPI
- Docker
- Kubernetes
- Minikube
- kubectl

## API Endpoints

### Home
GET /

### Prediction
POST /predict

Example Input:
{
  "value": 70
}

Example Output:
{
  "prediction": "High"
}