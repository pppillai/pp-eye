# Prepare Kubernetes Cluster 

- This involves the following steps:
    * Create the cluster using minikube.
    * Create the docker image for hello svc using minikube docker.
    * Create the pod and service deployment yaml.
    * Apply both the yaml.
    * Get the ip of the minikube cluster.
        * set the ip of minikube cluster and nodeport port as env variable for further use.

## Getting Started

* check if virtualization is supported
    > $ sysctl -a | grep -E --color 'machdep.cpu.features|VMX'
    VMX should be coloured.

* Install minikube
    > $ brew install minikube

* Check installation
    > $ minikube version

* Check status
    > $ minikube status

## Create the Cluster

* Start cluster
    > $ minikube start --driver=virtualbox

* Check status
    > $ minikube status

* Get clustor information
    > $ minikube kubectl -- get pods -A -o wide
    * At this point only master node should present.

## Prepare the Docker image in cluster

* ssh into the master node
    > $ minikube ssh (to ssh in the master)
* Check docker images 
    > $ docker image ls
* At this point there are only kubenetes created images.
    > exit

* switch to docker on minikube cluster node.
    > $ eval $(minikube docker-env)
* Create the docker image for the hello svc with minikube docker context.
    > docker  build -t hellosv:1.0 .
* Check if the image is present.
    > docker image ls

## Prepare the pod and svc deployment yaml files.
    - [pod](../configs/hello_svc_pod_deployment.yaml)
    - [service](../config/hello_svc_deployment.yaml)

## Deploy the container on pod and expose it.

* Getting Started.
    * To communicate with the cluster we are using kubectl

        >$ kubectl version

        >$ kubectl cluster-info
        
        > $ minikube ip
    * ip of minikube and kubernetes master should be same (return value from kubectl cluster-info cmd)

    * To check status of components
        >$ kubectl get componentstatus

    * To check nodes
        > $ kubectl get nodes

        > $ kubectl get nodes -o wide
    
    * This will show only the master as there are no apps deployed.

    * To check for pods
        > $ kubectl get pods

* Deploy
    * apply the config file to create the pod(pod_for_hello_binary.yaml)
        > $ kubectl apply -f configs/
    * To get info on all components
        > $ kubectl get all -o wide

