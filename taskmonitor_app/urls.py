from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.LoginView, name="login"),
    path("register", views.Register, name="register"),
    path("<str:username>/home/", views.Index, name="homepage"),
    path("<str:username>/calendar/", views.CalendarView, name="calendar"),
]
