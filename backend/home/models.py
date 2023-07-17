from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    hiii = models.BigIntegerField(blank=True,null=True,)
    hey = models.BigIntegerField(null=True,blank=True,)
