Q. Vegeta is being used to check performance of the APIs. How?
Q. Which tool you are  using to do security check on your APIs?
Q. Which methods you are using to test Code-Analysis in Golang, Sonar-Cube?
Q. Check that Glass-Door link you hae got and go through each line One by one by answering Questions.



Blackberry Spark work and Stuff.
https://www.blackberry.com/us/en/products/blackberry-spark-suites



# Introduction
Following Should be included in my Introduction as well:
We are seeking an upbeat self-starter to join our inclusive and globally distributed development team who is passionate about security related endpoint development. As a Senior Software Engineer, you will collaborate with product teams to turn business needs into solutions taking part in the entire software development lifecycle from conceptualization to deployment.

# My responsibilities

Design, develop, and debug - services, databases, and frontend applications.
#I do that.
Write well crafted, testable, performant, and efficient code.
# I do that.
Establish and promote design guidelines, best practices, and standards.
# I do that.
Mentor developers and assist with troubleshooting.
# I do that.
Craft a testing methodology unique to the application and its needs like, automated checks, test coverage of critical features, and maintaining production systems.
# I also do that.


# Working Experience:
Experience with designing software in Python and Golang.
## I have that , Python and Golang. (Also need to mention top 5 projects you worked with Python and Golang.)
Strong skills with cloud computing platforms such as AWS.
## yes, I do have with AWS, GCP and Azure! (Also check what kind of AWs and GCP feature there are.)
Experience with large-scale, distributed, event-based architectures.
## What kind of experience you have with that? (large-Scale, distributed and Event Based)
Ability to build REST based web APIs and/or event-driven consumers.
## Yes I do have that Ability as well.
Proficient with source control management, code reviews and continuous integration practices.
## Yes, GIT, Ansible, Jenkins, Build-pipelines.
Good understanding of microservices, domain driven design, integration patterns, scalable and resilient distributed cloud application architecture.
## I need to learn and understnad all that and how such thing are supposed to be handled Using
## Kubernetes, Kafka, Casandra, ELK and all.
Proven success collaborating in a fast-paced team environment using established agile development methodologies (such as Scrum, Kanban, etc.) against formal schedules.
## we are aprt of scrum team!, Do that alot.


So we are kind of resposible to create those frameworks like how it should be done.
What kind of Capabilities we should look for while designing that Framework and all.


domain driven design
Primary Focus on Business not technology or anything else.

integration patterns:



5 design Patterns Every engineer Should Know.
https://www.youtube.com/watch?v=FLmBqI3IKMA
1. Singleton
2. Fasad.
3. Bridge/Adapter (Abstraction Pattren!)
4. Strategy Pattren ()
5. Observer Pattren - Pub-Sub (Kafka!!!)

How Kafka Works?
https://www.youtube.com/watch?v=jY02MB-sz8I&list=PLa7VYi0yPIH2PelhRHoFR5iQgflg-y6JA&index=4


What i srequest Rate of your APIs?
It dependes on size of the packet and kind of environment we use while delvering the API.
For Goalng API testing we use vegeta.
https://github.com/tsenart/vegeta


API gateway Pattren:
https://microservices.io/patterns/apigateway.html


Right Now we are using Rancher.

https://rancher.com/

Just learn and understnad about Rancher!

We also use Traefik:
https://medium.com/@arshpreetsingh/hackers-guide-to-treafik-edge-router-1a2adb01c8db
Great-Idea of BlackHoles?


they think using that Blackhole soft-hair can account all the information store in the Black-hole.
Like how it does happen if it really happens?

My Idea: Using that work how to simulate a Black-hole in the system/computer?

Golang Security Notes while creating a Server.

You also need to learn more about TLS from following Link:
https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/
#Currently, the only acceptable TLS protocols are TLS 1.2 and TLS 1.3.
TLS = Transport Layer Security
SSL =

1. Crypto-TLS work!
* using these Mozilla Settings you need to know How to do things.
https://ssl-config.mozilla.org/#server=go&version=1.14.4&config=intermediate&guideline=5.6
* You have to force-redirect each request to HTTPS! (Run a Go-Routine for that!!)
* CipherSuites:(What is a Cipher-Suit?)
CipherSuites is a list of enabled TLS 1.0–1.2 cipher suites.
Need to know how many and where are those Cypher-Suites?
* ListenAndServeTLS() how to pass more variable to this?
-------------------
[Most-important]* However, you should still set PreferServerCipherSuites to ensure safer and
faster cipher suites are preferred, and CurvePreferences to avoid unoptimized
curves: a client using CurveP384 would cause up to a second of CPU to be consumed on our machines.

&tls.Config{
	// Causes servers to use Go's default ciphersuite preferences,
	// which are tuned to avoid attacks. Does nothing on clients.
	PreferServerCipherSuites: true,
	// Only use curves which have assembly implementations
	CurvePreferences: []tls.CurveID{
		tls.CurveP256,
		tls.X25519, // Go 1.8 only
	},
}
--------------
*Most-Secre with compatibility issues!.
MinVersion: tls.VersionTLS12,
	CipherSuites: []uint16{
		tls.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
		tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
		tls.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305, // Go 1.8 only
		tls.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,   // Go 1.8 only
		tls.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
		tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,

		// Best disabled, as they don't provide Forward Secrecy,
		// but might be necessary for some clients
		// tls.TLS_RSA_WITH_AES_256_GCM_SHA384,
		// tls.TLS_RSA_WITH_AES_128_GCM_SHA256,
	},

* Lucky-13 Atacks! (What is Luck-13 attack?)
How to avoid Lucky-13 attacks?

2.golang.org/x/crypto/acme/autocert package’s GetCertificate function.
* Important things while running on your local or any other service!
>>>>>>If you want to bind to a privileged port (ports less than 1024).
>>>>>>You either need to be root or have the CAP_NET_BIND_SERVICE capability.

setcap 'cap_net_bind_service=+ep' /path/to/program

setcap 'cap_net_bind_service=+ep' /usr/local/go/bin/go
SSL by default run on 443 Port.

authbind --deep ./autocert-server localhost

authbind --deep go run autocert-server.go localhost

sudo authbind --deep ./working-certs-server -domain dev.local.io



3. HSTS
This is the way to set headers!
w.Header().Set("Strict-Transport-Security", "max-age=15768000 ; includeSubDomains")
You need to know much more about setting headers and how to od that one way or other!!

4. Timeouts

Read Timeouts issues(sometimes)
>>>>>Sadly, ReadTimeout breaks HTTP/2 connections in Go 1.7. Instead of being reset
>>>>>for each request it's set once at the beginning of the connection and never reset,
>>>>>breaking all HTTP/2 connections after the ReadTimeout duration. It's fixed in 1.8.

A zero/default http.Server, like the one used by the package-level helpers
http.ListenAndServe and http.ListenAndServeTLS,
comes with no timeouts. You don't want that.

There are following three timeouts we need to mention/do....
4.1. ReadTimeout # start with making a connection
4.2. WriteTimeout # start with WriteTimeout normally covers the time from the end of the request header read to the end of the response write
However, when the connection is over HTTPS, SetWriteDeadline is called immediately after Accept
4.3. IdleTimeout

5. HTTP/2


Command to generate certifictes for localhost:
mkdir -p certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout certs/localhost.key -out certs/localhost.crt \
    -subj "/C=IND/ST=Punjab/L=Kutba/O=SDPS Chhapa/OU=Development/CN=localhost/emailAddress=arsh840@gmail.com"

Command to generate custom Domain certificate:

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout certs/localhost.key -out certs/dev.local.io.crt \
    -subj "/C=IND/ST=Punjab/L=Kutba/O=SDPS Chhapa/OU=Development/CN=localhost/emailAddress=arsh840@gmail.com"


1. You can generate your own certificate: https://marcofranssen.nl/build-a-go-webserver-on-http-2-using-letsencrypt
2. You could also use lego library for that!
https://go-acme.github.io/lego/
use following code to know more about Lego and stuff
file:///home/quantum-machine/Desktop/blackberry-project/mydata/use-the-acme-dns-challenge-to-get-a-tls-certificate.html
First learn about ListenAndServeTLS() in Goalng, Write your own server and make request
form LocalHost!

6. TCP Keep Alive

 tcpKeepAliveListener

 If you use ListenAndServe (as opposed to passing a net.Listener to Serve, which
 offers zero protection by default) a TCP Keep-Alive period of three minutes will
 be set automatically.

7. Server-mux
Package level functions like http.Handle[Func] (and maybe your web framework)
register handlers on the global http.DefaultServeMux which is used
if Server.Handler is nil. You should avoid that.

8. Metrics
9. Logging
