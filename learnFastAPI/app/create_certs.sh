#!/bin/sh
mkdir -p certs
openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:2048 -subj /CN=localhost -keyout certs/server.key -out certs/server.crt