from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    hi = models.BigIntegerField()
    hey = models.CharField(null=True,blank=True,max_length=256,)
