from django.db import models
from django.urls import reverse

class Sity(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('about_sity', kwargs={'sity': self.name})