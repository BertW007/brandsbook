from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_extensions import validators
from . import validators


class UserCreateForm(forms.ModelForm):
    post_code = forms.CharField(max_length=64, validators=[validators.post_code_validator])

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'company_name', 'post_code', 'city', 'street', 'nr', 'nip', 'phone']


class UserLoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()

        login = cleaned_data['login']
        password = cleaned_data['password']
        self.user = authenticate(username=login, password=password)

        if self.user is None:
            raise forms.ValidationError('Błędny login lub hasło')
        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    post_code = forms.CharField(max_length=64, validators=[validators.post_code_validator])

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'company_name', 'post_code', 'city', 'street', 'nr', 'nip', 'phone']


class SearchForm(forms.Form):
    company_name = forms.CharField(max_length=60)
