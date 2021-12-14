from django.db import models
import datetime
from django.contrib.auth.models import User


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField(blank=True)
    time = models.DateTimeField(blank=True ,default=datetime.datetime.now)
    def __str__(self):
        return self.username
class HomeContent(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(max_length=250, upload_to='homecontent/')
    content = models.TextField(blank=True)
    def _str__(self):
        return self.title
