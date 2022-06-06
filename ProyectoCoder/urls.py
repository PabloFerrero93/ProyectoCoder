
from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appCoder/', include('AppCoder.urls')),
]
