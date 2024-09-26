from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=75)
    ecn = models.CharField()
    ecndate = models.DateField(auto_now=False, auto_now_add=False)

    account = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    def formatDate(self):
        return self.subdate.strftime('%x')
    
    class Meta:
        ordering = ['ecndate']
