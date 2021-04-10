from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
class Organisation(models.Model):
    
    organisation_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    description = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default=NGOs,)
    certificate = models.FileField(
        upload_to='certificate/', null=True, verbose_name="")
    city = models.CharField(
        max_length=20, choices=CITY_CHOICES, default=LUCKNOW,)
    password = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    def __str__(self):
        return self.organisation_name

class Invitation(models.Model):
    #sender=models.OneToOneField(User,on_delete=models.CASCADE,related_name='sent_invitation')#senders invitation 
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_invitation')
    reciever=models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever_invitation')
    accepted_or_not=models.BooleanField(default=False)
    def _str_(self):
        return (self.sender.username+self.reciever.username)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def _str_(self):
        return self.name
