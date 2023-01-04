from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10,default='getachew')
   
    def __str__(self):
        return self.name

