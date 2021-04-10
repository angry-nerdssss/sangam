from django.db import models
from django import forms



"""class PasswordField(forms.CharField):
    widget = forms.PasswordInput
class PasswordModelField(models.CharField):
    def formfield(self, **kwargs):
        defaults = {'form_class': PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)"""


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
