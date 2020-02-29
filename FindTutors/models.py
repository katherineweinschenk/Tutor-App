from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BigUser(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 255)
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length = 500, default="")

    def __str__(self):  
        return "%s's profile" % self.user  


class Request(models.Model):
    sender = models.ForeignKey(BigUser,on_delete=models.CASCADE,related_name="BigUser_sender",blank=True,null=True)
    recipient = models.ForeignKey(BigUser,on_delete=models.CASCADE,related_name="BigUser_recipient",blank=True,null=True)
    subject = models.CharField(max_length = 500, default="")
    description = models.CharField(max_length = 500, default="")
    location = models.CharField(max_length = 500, default="")
