"""
WSGI config for Data project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Data.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

application = Cling(get_wsgi_application())






