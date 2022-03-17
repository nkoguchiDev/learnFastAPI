#!/bin/sh
mkdir -p backend/app/certs
openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:2048 -subj /CN=localhost -keyout backend/app/certs/server.key -out backend/app/certs/server.crt