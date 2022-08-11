from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='PARTNER CRUD OPERATIONS...!')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('emp/', include('employee.urls')),
    url(r'^$', schema_view)
    # path('emp/',include("employee.urls"))

]
# page -> is there resource -- which will be returned from the application method -->
# MVC -> url
# API --> uri --> uniform resource identifier --> method --> la --> never returns resource
