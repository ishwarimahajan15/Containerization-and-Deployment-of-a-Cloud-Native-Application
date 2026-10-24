$ErrorActionPreference = "Stop"

minikube status
if ($LASTEXITCODE -ne 0) { throw "Check Minikube status before deployment." }

minikube image load cloud-native-student-portal:1.0
if ($LASTEXITCODE -ne 0) { throw "Could not load the image into Minikube." }

kubectl apply -f k8s/deployment.yaml
if ($LASTEXITCODE -ne 0) { throw "Deployment apply failed." }

kubectl rollout status deployment/student-portal --timeout=120s
if ($LASTEXITCODE -ne 0) { throw "Deployment rollout did not complete." }

kubectl apply -f k8s/service.yaml
if ($LASTEXITCODE -ne 0) { throw "Service apply failed." }

kubectl get deployments
kubectl get pods -o wide
kubectl get services
Write-Host "For local access run: kubectl port-forward service/student-portal-service 8080:80"
