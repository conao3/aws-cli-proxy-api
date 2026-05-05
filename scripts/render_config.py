#!/usr/bin/env python3
import json
import os

api_key = os.environ["CLI_PROXY_API_KEY"]
management_key = os.environ.get("CLI_PROXY_MANAGEMENT_KEY", "")

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
''')
