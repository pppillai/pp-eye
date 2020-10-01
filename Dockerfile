FROM amd64/docker:latest

COPY ./hello .


EXPOSE 8080

ENTRYPOINT ["./hello"]