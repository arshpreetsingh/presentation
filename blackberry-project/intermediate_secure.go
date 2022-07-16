// generated 2022-06-25, Mozilla Guideline v5.6, Go 1.14.4, intermediate configuration
// https://ssl-config.mozilla.org/#server=go&version=1.14.4&config=intermediate&guideline=5.6
package main

import (
	"crypto/tls"
	"log"
	"net/http"
	"time"
	"golang.org/x/crypto/acme/autocert"
)

func main2() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		w.Header().Add("Strict-Transport-Security", "max-age=63072000")
		w.Write([]byte("This server is running the Mozilla intermediate configuration.\n"))
	})

	go func() {
		redirectToHTTPS := func(w http.ResponseWriter, req *http.Request) {
			http.Redirect(w, req, "https://"+req.Host+req.RequestURI, http.StatusMovedPermanently)
		}
		srv := &http.Server{
			Handler:     http.HandlerFunc(redirectToHTTPS),
			ReadTimeout: 60 * time.Second, WriteTimeout: 60 * time.Second,
		}
		log.Fatal(srv.ListenAndServe())
	}()

	m := &autocert.Manager{
		Cache:      autocert.DirCache("secret-dir"),
		Prompt:     autocert.AcceptTOS,
		Email:      "example@example.org",
		HostPolicy: autocert.HostWhitelist("localhost", "www.localhost"),
	}

	// Due to a lack of DHE support, you -must- use an ECDSA cert to support IE 11 on Windows 7
	cfg := &tls.Config{
		MinVersion: tls.VersionTLS12,
		CipherSuites: []uint16{
			tls.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
			tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
			tls.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
			tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
			tls.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,
			tls.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,
		},
	}

	srv := &http.Server{
		Addr:      ":443",
		Handler:   mux,
		TLSConfig: cfg,
		ReadTimeout: 5*time.Second,
		WriteTimeout: 10*time.Second,
		IdleTimeout: 120*time.Second,
		// Consider setting ReadTimeout, WriteTimeout, and IdleTimeout
		// to prevent connections from taking resources indefinitely.
	}

autocert.NewListener("localhost:5000"), mux)
	log.Fatal(srv.ListenAndServeTLS(autocert.NewLis":5000", nil))
}
