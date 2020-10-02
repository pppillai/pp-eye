# pp-eye
docker, kubernetes, python, go &amp; readme
* "pp-eye" project shows an approach to dockerize and deploy a service on kubernetes cluster.

* Given:
    * hello service default exposed port is 8080.
    * hello service accepts option -addr :portnumber

* Solution:
    > *all solution described are run on macOS Catalina(Darwin) 10.15.6*

- [Dockerize the service](/docs/DockerizeTheService.md)
- [Prepare Kubernetes cluster](/docs/PrepareKubernetes.md)
- [Run queries against the service](/docs/RunReport.md)
- [TL;DR](/docs/TLDR.md)

- Cli
    - devops task: python-cli
    - dev task: go-cli
    - qa task: checkout repo ppillai/armageddon
