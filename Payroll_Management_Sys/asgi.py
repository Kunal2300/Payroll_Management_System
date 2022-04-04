
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payroll_management_sys.settings')

application = get_asgi_application()
