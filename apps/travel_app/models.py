from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

