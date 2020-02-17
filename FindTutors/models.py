from django.db import models
from django.contrib.auth.models import AbstractUser
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

#types of the users
# class Tutor(models.Model):
#     user = models.OneToOneField(BigUser, on_delete = models.CASCADE, primary_key = True)
#     #dataase fields in the model
#     name_text = models.CharField(max_length = 200)
#     biography_text = models.CharField(max_length = 200)
#     reviews = models.CharField(max_length = 200)
#     number_of_people_tutored = models.IntegerField(default = 0)
#     STAR_RATING_CHOICES = (
#         (5, '5'),
#         ( 4, '4'),
#         (3,'3' ),
#         (2 , '2'),
#         (1 , '1'),
#         )
#     star_rating = models.IntegerField(choices=STAR_RATING_CHOICES, default=5)
#
#
# class Tutee(models.Model):
#     #database fields in the model
#     user = models.OneToOneField(BigUser, on_delete=models.CASCADE, primary_key=True)
#     name_text = models.CharField(max_length = 200)
#     introduction = models.CharField(max_length = 200)
#     subject = models.CharField(max_length =200)
#     avaialable_at = models.DateField(null=True, blank=True)


