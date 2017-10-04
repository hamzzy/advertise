from django import forms

from.models import Ads,UserProfile
from django.contrib.auth import (authenticate)

from django.contrib.auth.models import User



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AdvertForm (forms.ModelForm):

    class Meta:
        model=Ads
        fields=['name' ,'location','price','picture','category','phone','text']
        exclude = ['user']

class CreateForm (forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=('picture','location')




class Profile_edit(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['location','picture']

class User_edit(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
















