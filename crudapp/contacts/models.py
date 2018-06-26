from django.db import models


##Database Schema
#The model will be used to store contact information.
class Contacts(models.Model):
    cid = models.CharField(max_length=10) 
    name = models.CharField(max_length=50)  
    email = models.EmailField()  
    phone = models.CharField(max_length=15)