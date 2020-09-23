    
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,Group


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    signin_time=forms.DateTimeField()
    signout_time=forms.DateTimeField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username',
                  'password']




    def save(self):
        password = self.cleaned_data('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u

