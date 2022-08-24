# Poc_swagger
1. Implementation Notes:-                                                                                                                                                               1. Install django-rest-swagger                                                                                                                                       2. Add 'rest_framework_swagger' to INSTALLED_APPS in Django settings                                                                                                     3. In urls.py add from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]                                                                                                                                                                                                                                                                                                                                                     Links:-                                                                                                                                                                     https://django-rest-swagger.readthedocs.io/en/latest/       
