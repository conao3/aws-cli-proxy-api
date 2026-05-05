#!/usr/bin/env python3
import json
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: render_basic_auth.py SECRET_JSON")

    with open(sys.argv[1], "r", encoding="utf-8") as fh:
        payload = json.load(fh)

    users = payload.get("cli-proxy-api-basic-auth-users", "").strip()
    if not users:
        raise SystemExit("missing cli-proxy-api-basic-auth-users")

    print(users)


if __name__ == "__main__":
    main()
