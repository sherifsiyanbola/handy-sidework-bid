from django.db import models
from django.utils.timezone import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class serviceRequest(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class serviceRender(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # service_name = models.ForeignKey(serviceRequest, on_delete=models.CASCADE)
    service_name = models.ManyToManyField(serviceRequest)
    mycost = models.IntegerField()
    render_name = models.CharField(max_length=250)
    render_email = models.CharField(max_length=200)

    def __int__(self):
        return self.mycost

    class Meta:
        ordering = ['-id']