from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("", include("stands.urls", namespace="stands")),
    path("", include("reservas.urls", namespace="reservas")),
    path('admin/', admin.site.urls)
]
