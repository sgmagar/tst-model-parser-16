from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    hi = models.BigIntegerField()
    hey = models.BigIntegerField(null=True,blank=True,)
    shey = models.CharField(max_length=256,null=True,blank=True,)
