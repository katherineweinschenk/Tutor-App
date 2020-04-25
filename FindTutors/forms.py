from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TUser, Profile, Request, Reviews,TutorPosting
from django.forms import ModelForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms import bootstrap
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'address', 'latitude', 'longitude')
        widgets = {'latitude': forms.HiddenInput(), 'longitude': forms.HiddenInput()}

class TutorPostingForm(forms.ModelForm):
    class Meta:
        model = TutorPosting
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'year', 'bio', 'first_major', 'second_major','user_type']

class RegisterForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)


class TutorUserSignUpForm(forms.ModelForm):
    class Meta:
        model = TUser  # change model to TutorProfile and add bio
        fields = ['firstname', 'lastname',
                  'subjects',  'year', 'bio']
    SUBJECT_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Physics', 'Physics'),
        ('Math', 'Math'),
        ('English', 'English'),
        ('Algebra', 'Algebra'),
        ('Calculus', 'Calculus'),
        ('Geometry', 'Geometry'),
        ('Language', 'Language'),
        ('Reading', 'Reading'),
        ('Music', 'Music'),
    )
    widgets = {
        'firstname': forms.TextInput(
            attrs={                    'class': 'form-control'
            }
        ),
        'lastname': forms.TextInput(
            attrs={                    'class': 'form-control'
            }
         ),
         'subjects': forms.Select(
            choices=SUBJECT_CHOICES,attrs={
                'class': 'form-control'
            }
        ),
        'year': forms.NumberInput(
            attrs={                    'class': 'form-control'
            }
        ),
        'bio': forms.Textarea (
            attrs={                    'class': 'form-control'
            }
        ),
    }
#hello

class TuteeUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email',
                  'phone_number', 'year', 'subjects')


# TutorRegistrationForm
class TutorRegistration(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'phone_number', 'subjects')


# update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'year', 'user_type', 'first_major', 'second_major', 'bio']


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['profile', 'rating', 'reviews']
