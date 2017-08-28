from django import forms
from django_extensions import validators
from .models import User
from . import validators


class UserCreateForm(forms.ModelForm):
    nip = forms.CharField(64, validators=[validators.post_code_validator])

    class Meta:
        model = User
        fields = ['name', 'city', 'post_code', 'street', 'nr', 'email', 'phone']
