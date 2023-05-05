# Run Locally

## Create Dev Environment

* Clone the project
* Install minikube and kubectl
* Start minikube
* Create a namespace for the project

## Configure Kubernetes

* Create secret


    kubectl create secret docker-registry regcred \
        --docker-server=https://index.docker.io/v1/ \
        --docker-username=<username> \
        --docker-password=<password> \
        --docker-email=<email>

* Apply the api deployment


    kubectl apply -f manifests/deployment.yml