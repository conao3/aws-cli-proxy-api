# This repository intentionally keeps only the deployable container wrapper.
# The actual CLIProxyAPI binary and runtime are provided by the upstream image.
ARG CLI_PROXY_API_IMAGE=eceasy/cli-proxy-api:latest
FROM ${CLI_PROXY_API_IMAGE}
