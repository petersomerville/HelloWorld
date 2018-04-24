from django.db import models
from apps.travel_app.models import User

# Create your models here.

class BillItem(models.Model):
    description = models.CharField(max_length=128)
    amount = models.FloatField()

    user = models.ForeignKey(User, related_name = 'bills_of', on_delete=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
