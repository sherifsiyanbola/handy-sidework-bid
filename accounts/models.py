from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    
    phone_number = models.CharField(max_length=100)
    user_type = models.CharField( max_length = 250, choices= (
        ('In need of service', 'In need of service'),
        ('Service Provider', 'Service Provider')
    ))
    i_will_be_available_in = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.email