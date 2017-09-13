from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_extensions import validators
from .models import Detail, Brands, InterestingBrands
from . import validators


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


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


class UserCreateDetailForm(forms.ModelForm):
    post_code = forms.CharField(max_length=64, validators=[validators.post_code_validator])

    class Meta:
        model = Detail
        fields = ['company_name', 'post_code', 'city', 'street', 'nr', 'phone', 'nip']


class SearchForm(forms.Form):
    company_name = forms.CharField(max_length=60)


class SearchBrandsForm(forms.Form):
    brands = forms.CharField()


class AddBrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['name']


class BrandsCooperationForm(forms.Form):
    brands = forms.ModelChoiceField(queryset=InterestingBrands.objects.all())

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        super(BrandsCooperationForm, self).__init__(*args, **kwargs)
        if pk:
            self.fields['brands'].queryset = InterestingBrands.objects.filter(company=Detail.objects.filter(id=pk))
