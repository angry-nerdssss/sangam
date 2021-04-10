from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
class Organisation(models.Model):
    NGOs = 'NGOs'
    ORPHANAGE = 'ORPHANAGE'
    OLD_AGE_HOMES = 'OLD AGE HOMES'
    LUCKNOW = 'LUCKNOW'
    MUMBAI = 'MUMBAI'
    KOLKATA = 'KOLKATA'
    CHENNAI = 'CHENNAI'
    HYDERABAD = 'HYDERABAD'
    JAIPUR = 'JAIPUR'
    PUNE = 'PUNE'
    BANGLORE = 'BANGLORE'
    DELHI = 'DELHI'
    PATNA = 'PATNA'
    DEHRADUN = 'DEHRADUN'
    COIMBATORE = 'COIMBATORE'
    PRAYAGRAJ = 'PRAYAGRAJ'
    AYODHYA = 'AYODHYA'
    GANGTOK = 'GANGTOK'
    CATEGORY_CHOICES = [

        (NGOs, 'NGOs'),
        (ORPHANAGE, 'ORPHANAGE'),
        (OLD_AGE_HOMES, 'OLD AGE HOMES'),
    ]
    CITY_CHOICES = [
        (LUCKNOW, 'LUCKNOW'),
        (MUMBAI, 'MUMBAI'),
        (KOLKATA, 'KOLKATA'),
        (CHENNAI, 'CHENNAI'),
        (HYDERABAD, 'HYDERABAD'),
        (JAIPUR, 'JAIPUR'),
        (PUNE, 'PUNE'),
        (BANGLORE, 'BANGLORE'),
        (DELHI, 'DELHI'),
        (PATNA, 'PATNA'),
        (DEHRADUN, 'DEHRADUN'),
        (COIMBATORE, 'COIMBATORE'),
        (PRAYAGRAJ, 'PRAYAGRAJ'),
        (AYODHYA, 'AYODHYA'),
        (GANGTOK, 'GANGTOK'),
    ]
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


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def _str_(self):
        return self.name

class Invitation(models.Model):
    #sender=models.OneToOneField(User,on_delete=models.CASCADE,related_name='sent_invitation')#senders invitation 
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_invitation')
    reciever=models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever_invitation')
    accepted_or_not=models.BooleanField(default=False)
    def _str_(self):
        return (self.sender.username+self.reciever.username)


class Fund(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    phn = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zp = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Don(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    phn = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zp = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Hosting(models.Model):
    # sender=models.OneToOneField(User,on_delete=models.CASCADE,related_name='host_s')#senders invitation 
    
    # reciever=models.OneToOneField(User,
    #         on_delete=models.CASCADE, related_name='host_r')
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='host_s')
    reciever=models.ForeignKey(User, on_delete=models.CASCADE,related_name='host_r')
    meeting_date=models.DateField()
    venue=models.CharField(max_length=100)
    feedback_done=models.BooleanField(default=False)
    def _str_(self):
        return (self.sender.username+self.reciever.username)

class Feedback_after_event(models.Model):
    feedback_by=models.ForeignKey(Organisation, on_delete=models.CASCADE,related_name='feedback_r')
    feedback_for=models.ForeignKey(Organisation, on_delete=models.CASCADE,related_name='feedback_s')
    how_day=models.CharField(max_length=100)
    how_other=models.CharField(max_length=100)
    rate=models.IntegerField()
    def _str_(self):
        return self.how_other