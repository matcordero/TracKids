from django.utils import timezone
from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    birtDate = models.DateTimeField(default=timezone.now)
    email = models.EmailField(primary_key=True)
    password = models.TextField()
    icon = models.TextField()
    keyValidate = models.CharField(max_length=100, null=True, blank=True)
    
    