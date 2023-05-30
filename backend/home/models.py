from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    hi = models.BigIntegerField()
    hey = models.CharField(max_length=256,null=True,blank=True,)
