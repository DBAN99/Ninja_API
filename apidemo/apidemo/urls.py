from django.contrib import admin
from django.urls import path
from .api import api
from .crudapi import crudapi



urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("crudapi/", crudapi.urls),
]