from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")

    phone = models.CharField(max_length=35, verbose_name="phone number", **NULLABLE)
    avatar = models.ImageField(upload_to='media/', verbose_name='avatar', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name="token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
