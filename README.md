# pp-eye
docker, kubernetes, python, go &amp; readme
* "pp-eye" project shows an approach to dockerize and deploy a service on kubernetes cluster.
* cli written in golang and python

* Given:
    * hello service default exposed port is 8080.
    * hello service accepts option -addr :portnumber
    * hello service accepts a single argument for get call and returns the "Hi there, <arg>!"

* Solution:
    > *all solution described are run on macOS Catalina(Darwin) 10.15.6*

- [TL;DR](/docs/TLDR.md)

- [Dockerize the service](/docs/DockerizeTheService.md)

- [Prepare Kubernetes cluster](/docs/PrepareKubernetes.md)

- [Run queries against the service](/docs/RunReport.md)

- Cli
    - devops task: [python-cli](/docs/PythonCli.md)
    - dev task: [go-cli](/docs/GoCli.md)
    - qa task: [armageddon](https://github.com/pppillai/armageddon)

- CodeFile Links
    - [pod yaml](/configs/hello_svc_pod_deployment.yaml)
    - [service yaml](/configs/hello_svc_deployment.yaml)
    - [pycli](/pycli/pycli.py)
    - [gocli](/gocli/hello.go)
