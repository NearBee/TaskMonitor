from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("<str:username>/home/", views.index, name="homepage"),
    path("<str:username>/calendar", views.calendar_view, name="calendar"),
]
