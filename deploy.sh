#!/usr/bin/env bash

echo "Creating deployment archive"
zip -r cloud-functions.zip ./src

echo "Creating login function"
yc serverless function create --name=login --description "Logs in existing users"

echo "Make login function public"
yc serverless function allow-unauthenticated-invoke login

echo "Deploying latest code to login function"
yc serverless function version create \
--function-name=login \
--runtime python37 \
--entrypoint src.handlers.login.handler \
--memory 128m \
--execution-timeout 3s \
--source-path ./cloud-functions.zip

echo "Deploying API Gateway"

# create if does not exist
yc serverless api-gateway create \
--name="autowebinar" \
--description="Autowebinar API" \
--spec=api-gateway.yaml

# update if already exists
yc serverless api-gateway update \
--name="autowebinar" \
--description="Autowebinar API" \
--spec=api-gateway.yaml

echo "DONE!"