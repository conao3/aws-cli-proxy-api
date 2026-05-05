# aws-cli-proxy-api

Container and Kubernetes deployment definitions for [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) on conao3's `aws-infra-k8s` cluster.

This repository does not vendor CLIProxyAPI source code. It wraps the upstream Docker image and deploys it to the existing Kubernetes infrastructure.

## Runtime

- Upstream image: `eceasy/cli-proxy-api:latest`
- Internal port: `8317`
- Public ingress paths:
  - `/v1`
  - `/api/provider`
- Host: `dev-cli-proxy-api.sancode.dev`
- Auth/config/log persistence:
  - config: Kubernetes Secret `cli-proxy-api-config`
  - auth files: EFS PVC `cli-proxy-api-auths`
  - logs: EFS PVC `cli-proxy-api-logs`

## Required Secrets Manager keys

The deploy build reads `${PREFIX}-secret` and expects:

- `cli-proxy-api-key`: downstream API key for clients
- `cli-proxy-api-management-key`: optional management key for localhost/port-forwarded management API or UI
- `cli-proxy-api-basic-auth-users`: nginx `auth_basic_user_file` content for the public ingress basic authentication proxy

Management remote access is disabled in the rendered config. If `cli-proxy-api-management-key` is empty, `/v0/management/*` stays disabled. Use `kubectl port-forward` plus a management key, or `kubectl exec`, for OAuth and management work.

## Build and deploy

The `aws-infra-k8s` stack creates CodeBuild projects and Step Functions for this repository.

- build: builds the wrapper image and pushes `${PREFIX}-cli-proxy-api:latest`
- deploy: renders config from Secrets Manager, applies `k8s/cli-proxy-api`, updates the deployment image, and waits for rollout
- the default build base image is `${ECR_REGISTRY}/${PREFIX}-cli-proxy-api:upstream`, so bootstrap that tag once from a machine that can pull `eceasy/cli-proxy-api:latest`

Before the first CodeBuild run, push this repository to the GitHub location referenced by `aws-infra-k8s`: `https://github.com/conao3/aws-cli-proxy-api.git`.

## Local validation

```bash
CLI_PROXY_API_KEY=dummy CLI_PROXY_MANAGEMENT_KEY=dummy python3 scripts/render_config.py > /tmp/config.yaml
kubectl kustomize k8s/cli-proxy-api
```
