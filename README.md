# Why?

This is a simple demo of how to set up a Kubernetes cluster with a single service. The kluster contains a single pod
that needs to be pre-compiled and pushed to a docker registry. The pod is then deployed to the cluster and exposed as
a service.

# How?

## Create MiniKube cluster

* Clone the project
* Install minikube and kubectl
* Start minikube
* Create a namespace for the project

## Configure Kubernetes

* Create secret for docker registry


    kubectl create secret docker-registry regcred \
        --docker-server=https://index.docker.io/v1/ \
        --docker-username=<username> \
        --docker-password=<password> \
        --docker-email=<email>

* Apply the api deployment


    kubectl apply -f manifests/deployment.yml

* Create a MiniKube service that will act as an ingress (due to the lack of a real ingress controller)


    minkube service api --url


