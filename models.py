from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FavoriteQuote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='favourite_quote')
    quote=models.TextField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return f"'{self.quote}' by {self.author}"
