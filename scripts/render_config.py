#!/usr/bin/env python3
import json
import os
import sys


def load_config():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as fh:
            payload = json.load(fh)
        return (
            payload["cli-proxy-api-key"],
            payload.get("cli-proxy-api-management-key", ""),
        )
    return (
        os.environ["CLI_PROXY_API_KEY"],
        os.environ.get("CLI_PROXY_MANAGEMENT_KEY", ""),
    )


api_key, management_key = load_config()

print(f'''host: ""
port: 8317

tls:
  enable: false
  cert: ""
  key: ""

remote-management:
  allow-remote: false
  secret-key: {json.dumps(management_key)}
  disable-control-panel: false
  disable-auto-update-panel: true

auth-dir: "/root/.cli-proxy-api"

api-keys:
  - {json.dumps(api_key)}

debug: false
logging-to-file: true
logs-max-total-size-mb: 512
error-logs-max-files: 20
usage-statistics-enabled: false

proxy-url: ""
request-retry: 3
max-retry-interval: 30
ws-auth: true

routing:
  strategy: "round-robin"
  session-affinity: true
  session-affinity-ttl: "1h"
''')
