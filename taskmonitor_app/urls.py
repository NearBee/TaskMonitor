from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.creation, name="creation"),
    path("home/", views.index, name="homepage"),
]