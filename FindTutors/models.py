from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone

# class MyUser(AbstractUser):
#     is_tutee = models.BooleanField('student status', default=False)
#     is_tutor = models.BooleanField('teacher status', default=False)

class BigUser(AbstractUser):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 255)
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length = 500, default="")

class Request(models.Model):
    sender = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_sender",blank=True,null=True)
    recipient = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_recipient",blank=True,null=True)
    subject = models.CharField(max_length = 500, default="")
    description = models.CharField(max_length = 500, default="")
    location = models.CharField(max_length = 500, default="")

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(BigUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __unicode__(self):
        return self.message


# class Tutee(models.Model):
#     #database fields in the model
#     user = models.OneToOneField(BigUser, on_delete=models.CASCADE, primary_key=True)
#     name_text = models.CharField(max_length = 200)
#     introduction = models.CharField(max_length = 200)
#     subject = models.CharField(max_length =200)

#     avaialable_at = models.DateField(null=True, blank=True)

