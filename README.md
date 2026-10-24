# Cloud-Native Student Portal

## Objective
Containerize a small Python web application using Docker and prepare it for deployment on Kubernetes. The application serves a student portal landing page and a health-check endpoint.

## Technologies
- Python 3.12
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Project structure
```text
cloud-native-student-portal/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

## Run with Docker
Build the image:
```powershell
docker build -t cloud-native-student-portal:1.0 .
```

Run the container:
```powershell
docker run -d --name student-portal-container -p 5000:5000 cloud-native-student-portal:1.0
```

Verify the container:
```powershell
docker ps
```

Open:
- Application: http://localhost:5000
- Health check: http://localhost:5000/health

To view logs:
```powershell
docker logs student-portal-container
```

To stop the container:
```powershell
docker stop student-portal-container
```

## Kubernetes deployment with Minikube
Ensure Docker Desktop is running and Minikube reports the host, kubelet and API server as Running before continuing.

Start the cluster:
```powershell
minikube start --driver=docker
kubectl get nodes
```

Load the locally built image:
```powershell
minikube image load cloud-native-student-portal:1.0
```

Deploy the application and Service:
```powershell
kubectl apply -f k8s/deployment.yaml
kubectl rollout status deployment/student-portal
kubectl apply -f k8s/service.yaml
```

Verify resources:
```powershell
kubectl get deployments
kubectl get pods -o wide
kubectl get services
```

Access the application through the Service using port forwarding:
```powershell
kubectl port-forward service/student-portal-service 8080:80
```

Keep that terminal open, then visit:
- Application: http://localhost:8080
- Health check: http://localhost:8080/health

## Kubernetes configuration
- Deployment requests two replicas.
- Readiness and liveness probes use `/health`.
- CPU and memory requests/limits are defined.
- A NodePort Service exposes port 80 and forwards traffic to container port 5000.

## Evidence checklist
Capture your own screenshots after verifying each step:
1. Successful Docker image build.
2. `docker ps` showing the running application container.
3. Browser showing the application at `http://localhost:5000`.
4. `minikube status` and `kubectl get nodes` showing a healthy cluster.
5. `kubectl get pods` showing two Running pods.
6. `kubectl get services` showing `student-portal-service`.
7. Browser showing the application at `http://localhost:8080`.
8. Public GitHub repository containing the project files.

Only include screenshots of results you actually achieved. Do not claim Kubernetes deployment succeeded until the cluster is healthy and the application has been tested.
