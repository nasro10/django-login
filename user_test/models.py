from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Usert(models.Model):
    nom =models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.nom +  '  '+self.prenom


class UserProfile(models.Model):
    user=models.OneToOneField(User)
    adresse = models.CharField(max_length=250)

#kwargs :c'est le keyword argument
def create_profile(sender,**kwargs):
    if kwargs['created']:
       user_profile= UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile,sender=User)
