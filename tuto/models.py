from django.db import models

# Create your models here.
class ApiModel(models.Model):
    description = models.TextField(max_length=1000, blank=False, null=False)
    url = models.CharField(max_length=100, blank=False, null=False)
