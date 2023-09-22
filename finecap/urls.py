from django.contrib import admin
from django.urls import path
from stands.views import *


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls)
]