package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {

	// hardcode values for Env variables
	nodeport := os.Getenv("NODEPORTPORT")
	clusterip := os.Getenv("KUBECLUSTERIP")

	if len(nodeport) == 0 {
		panic("nodeport is not set")
	}
	if len(clusterip) == 0 {
		panic("cluster ip is not set")
	}

	// parse command line
	flag.Parse()
	name := flag.Arg(0)

	// do the call
	url := fmt.Sprintf("http://%s:%s/%s", clusterip, nodeport, name)
	resp, err := http.Get(string(url))

	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	log.Println(string(body))
}
