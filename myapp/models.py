from django.db import models
import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class animal (models.Model):

    #author=models.Foreignkey(User , default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    #slug=models.SlugField(default=None)
    sex_cho=[('M','Male'),('F','Female')]
    name=models.CharField(max_length=100)
    kingdom=models.CharField(max_length=100,blank=True)
    sex=models.CharField(max_length=1,choices=sex_cho)
    description=RichTextField()
    #dob=models.DateTimeField(default=datetime.date.today)
    age=models.IntegerField(null=True)
    vaccinations=models.ManyToManyField('vaccine',blank=True)

    DOB=models.DateField(max_length=8, default=datetime.date.today)
    img=models.ImageField(upload_to='media' , default='empty.png', blank=True)
    #title=models.CharField(default='animal.name',max_length=100)
    #thumb=mode#ls.ImageField(default='empty.png',blank='True')

    def __str__(self):
        return self.kingdom

    def snip(self):
        #sniip=self.description[:30] +'...'
        return (self.description[:30]+' ...')

    def backage(self):
        return self.DOB.year

class Pics(models.Model):
    img=models.ImageField(default='empty.png' , blank=True)


class vaccine(models.Model):
    name=models.CharField(max_length=60)
    #thumb=models.ImageField(default='empty.png',blank='True')
    def __str__(self):
        return self.name
class sort(models.Model):
    tail=models.CharField(max_length=4)
    def __str__(self):
      return self.name
