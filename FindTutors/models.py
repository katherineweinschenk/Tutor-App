from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager

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


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser):
        if not email:
            raise ValueError('user must have email address')
        email = self.normalize_email(email)
        user = self.model(username=username,
            email=email,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser,
        )
        # We check if password has been given
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


# We change following functions signature to allow "No password"
    def create_user(self, username, email, password=None):
        return self._create_user(username, email, password, False, False)

    def create_superuser(self, username, email, password=None ):
        user= self._create_user(username, email, password, True, True)
        user.save(using=self._db)
        return user


    # def create_superuser(self, email, username=None, **extra_fields):
    #     user = self._create_user(email, username, True, True, **extra_fields)
    #     user.save(using=self._db)
    #     return user

class TUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 200,default = '0')
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True, null=True)
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)
    year = models.IntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=500, default="")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    objects =  UserManager()



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# class Request(models.Model):
#     sender = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_sender",blank=True,null=True)
#     recipient = models.ForeignKey(BigUser,models.SET_NULL,related_name="BigUser_recipient",blank=True,null=True)
#     subject = models.CharField(max_length = 500, default="")
#     description = models.CharField(max_length = 500, default="")
#     location = models.CharField(max_length = 500, default="")

class Request(models.Model):
    sender = models.ForeignKey(TUser,models.SET_NULL,related_name="TUser_sender",blank=True,null=True)
    recipient = models.ForeignKey(TUser,models.SET_NULL,related_name="TUser_recipient",blank=True,null=True)
    subject = models.CharField(max_length = 500, default="")
    description = models.CharField(max_length = 500, default="")
    location = models.CharField(max_length = 500, default="")

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __unicode__(self):
        return self.message