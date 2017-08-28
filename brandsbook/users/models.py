from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    nip = models.IntegerField()
    city = models.CharField(max_length=64)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=64)
    nr = models.CharField(max_length=16)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
