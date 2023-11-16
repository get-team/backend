from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stores/", views.get_store_list, name="get_store_list")
]