from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("get_eco/", include("get_eco.urls")),
    path('admin/', admin.site.urls),
]
