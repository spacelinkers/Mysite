from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm,
)

from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class EditUserInfoForm(forms.ModelForm):
    city = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'city...',
        }
    ))
    website = forms.URLField(widget = forms.URLInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'website...'
        }
    ))
    phone = forms.IntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'phone...'
        }
    ))
    profile_image = forms.ImageField()
    

    class Meta:
        model = UserProfile
        fields = (
            'city',
            'website',
            'phone',
            'profile_image',
        )
          

    