package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func data(w http.ResponseWriter, r *http.Request) {
	fmt.Println("this is my HTTP WOrk!")
	fmt.Println("this is my cypher suit Name!->", tls.CipherSuiteName)
}

func main2() {
	http.HandleFunc("/", data)
	http.ListenAndServe(":5000", nil)
}
