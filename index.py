from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle_request
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_23758042.settings")

application = get_wsgi_application()

def handler(request, context):
    return handle_request(request, application)
