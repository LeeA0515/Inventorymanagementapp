from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    topic = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    poster = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.topic
    
    def formatDate(self):
        return self.date.strftime('%c')

    class Meta:
        ordering = ['-date']