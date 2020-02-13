from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
        return user


class TuteeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def save(self):
        user = super().save(commit=False)
        user.is_tutee = True
        user.save()
        return user