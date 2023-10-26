from django.shortcuts import render
from .models import User

# Create your views here.


def login(username):
    user = User.objects.create_user(username=username, password=password)
