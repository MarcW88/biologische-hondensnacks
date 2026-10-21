#!/usr/bin/env python3
"""Local machine adapter; does not replace the original editorial workflow."""
from scripts.validate_content_workflows import validate
if __name__ == '__main__':
    raise SystemExit(validate('usage', publish=True))
