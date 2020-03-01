from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# class BigUser(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     firstname = models.CharField(max_length = 200)
#     lastname = models.CharField(max_length = 200)
#     email = models.EmailField(max_length = 255)
#     phone_number = models.IntegerField(blank=True, null=True)
#     is_tutee = models.BooleanField('student status', default=False)
#     is_tutor = models.BooleanField('teacher status', default=False)
#     year = models.IntegerField(blank=True, null=True)
#     subjects = models.CharField(max_length = 500, default="")
#
#     def __str__(self):
#         return "%s's profile" % self.user

class TUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=500, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname','phone_number', 'year','subjects']

# class Request(models.Model):
#     sender = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_sender",blank=True,null=True)
#     recipient = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_recipient",blank=True,null=True)
#     subject = models.CharField(max_length = 500, default="")
#     description = models.CharField(max_length = 500, default="")
#     location = models.CharField(max_length = 500, default="")

class Request(models.Model):
    sender = models.ForeignKey(TUser,models.SET_NULL,related_name="BigUser_sender",blank=True,null=True)
    recipient = models.ForeignKey(TUser,models.SET_NULL,related_name="BigUser_recipient",blank=True,null=True)
    subject = models.CharField(max_length = 500, default="")
    description = models.CharField(max_length = 500, default="")
    location = models.CharField(max_length = 500, default="")