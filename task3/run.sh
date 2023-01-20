#!/bin/bash

docker build -t task3/api1 ./api1

docker build -t task3/api2 ./api2

docker build -t task3/bff ./bff

kubectl apply -f ./api1/api1-deployment.yml -f ./api1/api1-service.yml -f ./api2/api2-deployment.yml -f ./api2/api2-service.yml -f ./bff/bff-deployment.yml -f ./bff/bff-service.yml -f ./ingress.yml