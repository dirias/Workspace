from typing_extensions import Required
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Card(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    front = models.CharField(max_length=150, Required=True)
    back = models.CharField(max_length=400, Required=True)
    deck_name = models.CharField(max_length=100, Required=True)
    category = models.CharField(max_length=100, Required=True)
    active_deck = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)
    tag = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.front