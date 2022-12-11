# Chalice Example

## Requirements

- python 3.7 and 3.9
- poetry
- terraform 1.1.9

## How to use?

- put all python code into example/chalicelib, initialize app in app.py
- put all stateful deployments into infra
- configure both terraform backends
- configure config.py with environment variables to pass into lambda functions
- use run script for all commands

## Deployment flow

- initialize and apply terraform from main infra folder
- run config.py to get terraform outputs and pass them to config.json
- generate requirements.txt from pyproject.toml
- generate terraform deployment with chalice
- run config_backend.py to setup backend for this deployment
- initialize and apply terraform from example/infra
- connect API Gateway to DNS record manually

## Advantages

- lambdas, layers, roles and API Gateway is generated with chalice
- easy to use handlers, good integration with AWS environment
- seems faster than similarly designed API using FastAPI (lower package size?)
- local server for testing uses real AWS credentials to connect to the account

## Disadvantages

- complicated deployment, requires custom scripts to pass all values and
  modification of a lot of files to introduce changes
- a lot of things are automatically generated so we need to remember to do it
  before PR to have all deployed changes in the repo itself
- rigid project structure, might not be extensible for larger applications
- after successful deployment, proper API Gateway needs to be connected to
  Route53 separately, chalice only configures API Gateway to use proper DNS but
  it doesn't create or change DNS records

## Notes

(after setting up infra only, python API functionalities not yet properly tested)

This config is useful for small and personal projects only because of the huge
configuration effort to make it work with many different environments (stg,
prd). Also the project structure is very rigid and everything needs to be done
in the chalice way.

Configuration is quite complicated for start and I don't think (yet) that the
automatic IaC generation via chalice is worth it. It might be when adding the
whole python framework into account but this needs to be further tested.

Personal quick projects (without terraform) - perfect.
Huge company projects with very custom internal deployments - not so much.

Ideally if the provided API functions are good by itself it might be worth taking
those and implementing into the python codebase without using the whole
framework.

example works as a main or sub app, more similar can be added and managed
separately to manage different contexts but domain configuration will be harder
in this case and probably not worth the effort as we would have to maintain
another API Gateway deployment and configuration separate from the main infra deployment.
