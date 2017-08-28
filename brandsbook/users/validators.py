from django import forms


def post_code_validator(value):
    if not value('\d\d\-\d\d\d'):
        raise forms.ValidationError('Invalid post code')
