$ErrorActionPreference = "Stop"

docker build -t cloud-native-student-portal:1.0 .
if ($LASTEXITCODE -ne 0) { throw "Docker image build failed." }

$existing = docker ps -a --filter "name=^student-portal-container$" --format "{{.Names}}"
if ($existing -eq "student-portal-container") {
    docker rm -f student-portal-container
}

docker run -d --name student-portal-container -p 5000:5000 cloud-native-student-portal:1.0
docker ps
Write-Host "Open http://localhost:5000 and http://localhost:5000/health"
