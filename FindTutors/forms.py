from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  BigUser, Request
from django.forms import ModelForm
#
# class TutorSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Tutor
#         # fields = ('firstname', 'lastname', 'email', 'phone_number')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_tutor = True
#         if commit:
#             user.save()
#         return user
#
#
# class TuteeSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Tutee
#         # fields = ('firstname', 'lastname', 'email', 'phone_number')
#
#     def save(self):
#         user = super().save(commit=False)
#         user.is_tutee = True
#         user.save()
#         return user

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'location',)

class TutorUserSignUpForm(UserCreationForm):
    class Meta:
        model = BigUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_tutor = True
    #     if commit:
    #         user.save()
    #     return user

class TuteeUserSignUpForm(UserCreationForm):
    class Meta:
        model = BigUser
        fields= ('firstname', 'lastname', 'email', 'phone_number',)
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_tutee = True
    #     if commit:
    #         user.save()
    #     return user