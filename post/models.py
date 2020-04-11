from django.db import models

# Create your models here.
class Pics(models.Model):
    img=models.ImageField(default='empty.png' , blank=True)
