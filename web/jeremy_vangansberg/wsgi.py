"""
WSGI config for jeremy_vangansberg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import pathlib

import dotenv

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))

from jeremy_vangansberg.settings import base

if base.DEBUG :
    settings_path = 'jeremy_vangansberg.settings.dev'
else :
    settings_path = 'jeremy_vangansberg.settings.prod'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

application = get_wsgi_application()
