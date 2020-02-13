from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_tutee = models.BooleanField('student status', default=False)
    is_tutor = models.BooleanField('teacher status', default=False)