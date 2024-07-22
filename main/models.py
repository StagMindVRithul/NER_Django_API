from django.db import models
from django.contrib.auth.models import User 


class Medical(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    entities = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author + "\n" + self.text
