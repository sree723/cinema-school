from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "department/<str:department_name>/",
        views.department,
        name="department"
    ),
]