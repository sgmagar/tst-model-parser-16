from django.conf import settings
from django.db import models
class Hello(models.Model):
    'Generated Model'
    hi = models.BigIntegerField()
    hey = models.BigIntegerField(null=True,blank=True,)
class Hi(models.Model):
    'Generated Model'
    how = models.BigIntegerField()
    why = models.BigIntegerField(null=True,blank=True,)
