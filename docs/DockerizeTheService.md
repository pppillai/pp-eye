# Dockerize hello service

* Given:
    * hello service default exposed port is 8080.
    * hello service accepts option -addr :<port>

* Steps:
    * Create a new directory say pp-op-assign.
    * Copy the hello servie binary to the directory.
    * Create a docker file Dockerfile. - [Dockerfile](../Dockerfile)
    * Run the following docker command:
        > $ docker build -t hellobinaryfinal:0.0.1 .
    * This will create the image in local repository.
    * Verify image is present in the local repository.
        > $ docker image ls

    * Run the following docker command:
        > $ docker run -it -p 9090:9090 --expose 9090 hellobinaryfinal:0.0.1 -addr :9090

            > 9090:9090 = <localhost port>:<docker container port>
            > --expose 9090 = docker container port
            > -addr :9090 = need for the service to listen to any port other than 8080

    * Verify the container is running.
        > $ docker container ls

