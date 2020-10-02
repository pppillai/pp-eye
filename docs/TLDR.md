# Quick Setup and Run

## Quick Setup
* Start cluster
    > $ minikube start --driver=virtualbox
* Switch to docker on minikube cluster node.
    > $ eval $(minikube docker-env)
* Create the docker image for the hello svc with minikube docker context.
    > docker  build -t hellosv:1.0 .
* Deploy
    * Apply the config file to create the pod and service.
        > $ kubectl apply -f configs/
    * To get info on all components
        > $ kubectl get all -o wide
    * To get the ip of the cluster
        > $ minikube ip
* Export the ip address of cluster and port of Nodeport service
    > export KUBECLUSTERIP=<Check response of cmd "minikube ip">
    > export NODEPORTPORT=31313
* Run command in gocli folder
    > $ go build hello.go
    > $ ./hello "pradeep"
    > $ ./hello
* Run command in pycli folder
    > $ python3 -m venv env
    > $ . env/bin/activate
    > $ pip install --editable .
    > $ hello
    > $ hello "pradeep"

