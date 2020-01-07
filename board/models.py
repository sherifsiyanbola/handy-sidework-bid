from django.db import models
from django.utils.timezone import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class serviceProvider(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class serviceRender(models.Model):
    # manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # service_name = models.ForeignKey(serviceRequest, on_delete=models.CASCADE)
    service_name = models.ForeignKey(serviceProvider, on_delete=models.CASCADE, default=True)
    mycost = models.IntegerField()
    render_name = models.CharField(max_length=250)
    render_email = models.CharField(max_length=200)
    location = models.CharField(max_length=250, blank=True)
    are_you_available = models.CharField(max_length=50, blank=True)

    def __int__(self):
        return self.mycost

    class Meta:
        ordering = ['-id']