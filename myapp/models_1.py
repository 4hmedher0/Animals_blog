from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class animal (models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE,default='AHMED')
    sex_cho=[('M','Male'),('F','Female')]
    name=models.CharField(max_length=100)
    kingdom=models.CharField(max_length=100,blank=True)
    sex=models.CharField(max_length=1,choices=sex_cho)
    description=models.TextField(max_length=1400)
    dob=models.DateTimeField(default=datetime.date.today)
    age=models.IntegerField(null=True)
    DOB=models.DateField(max_length=8, default=datetime.date.today)
    #img=models.ImageField(upload_to='.animals_pics' , default='empty.png', blank=True)
    #thumb=models.ImageField(default='empty.png',blank='True')
    #title=models.CharField(default='animal.name',max_length=100)

    vaccinations=models.ManyToManyField('vaccine',blank=True)
    def __str__(self):
        return self.kingdom

    def snip(self):
        #sniip=self.description[:30] +'...'
        return (self.description[:30]+' ...')

    def backage(self):
        return self.DOB.year



class vaccine(models.Model):
    name=models.CharField(max_length=60)
    def __str__(self):
        return self.name
class sort(models.Model):
    tail=models.CharField(max_length=4)
    def __str__(self):
      return self.name
