from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    display_name = models.CharField(max_length=24, unique=True, blank=False, null=False)
