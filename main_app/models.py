from django.db import models
from django.urls import reverse

# Create your models here.


class Wish(models.Model):
    wish = models.TextField(max_length=200)

    def __str__(self):
        return self.wish
    
    def get_absolute_url(self):
        return reverse('wishes_detail', kwargs={'wish_id': self.id})