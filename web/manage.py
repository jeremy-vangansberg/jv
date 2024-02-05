#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
import pathlib

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

def main():
    if DEBUG :
        settings_path = 'jeremy_vangansberg.settings.dev'
    else :
        settings_path = 'jeremy_vangansberg.settings.prod'
    """Run administrative tasks."""
    print('manage',settings_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    dotenv.read_dotenv()
    DEBUG = os.getenv('DEBUG') == '1'
    main()
