from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Router

api = NinjaAPI()

first_router = Router()
second_router = Router()
third_router = Router()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@first_router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@second_router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@third_router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


second_router.add_router("l3", third_router)
first_router.add_router("l2", second_router)
api.add_router("l1", first_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]