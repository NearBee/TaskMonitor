from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("home/", views.index, name="homepage"),
]
