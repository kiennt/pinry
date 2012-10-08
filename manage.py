#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    PINRY_ENVIRONMENT = os.environ.get("PINRY_ENVIRONMENT", "development")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pinry.settings.%s" % PINRY_ENVIRONMENT)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
