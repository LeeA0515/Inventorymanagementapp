from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=75)
    referenceId = models.CharField()
    quantity = models.IntegerField()
    parlevel = models.IntegerField()
    expdate = models.DateField(auto_now=False, auto_now_add=False)

    account = models.ForeignKey(User, on_delete=models.DO_NOTHING) 

    def __str__(self):
        return self.name

class Request(models.Model):
    namer = models.CharField(max_length=75)
    referenceIdr = models.CharField()
    quantityr = models.IntegerField()
    comment = models.TextField()
    subdate = models.DateTimeField()
    completed = models.BooleanField(default=False)

    account = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.namer