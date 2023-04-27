from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=75)
    referenceId = models.CharField()
    quantity = models.IntegerField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
