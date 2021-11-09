#!/usr/bin/env python3

import json
import os

print(f"Operating system: {os.getenv('RUNNER_OS')}")

print(json.dumps(dict(os.environ), indent=4))
