from django.contrib.auth.models import User
from django.db import models


class Detail(models.Model):
    person = models.OneToOneField(User)
    company_name = models.CharField(max_length=64)
    nip = models.CharField(max_length=10)
    city = models.CharField(max_length=64)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=64)
    nr = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)


class Brands(models.Model):
    name = models.CharField(max_length=128)
    company = models.ManyToManyField(Detail)

    def __str__(self):
        return self.name


class InterestingBrands(models.Model):
    name = models.CharField(max_length=128)
    company = models.ManyToManyField(Detail)

    def __str__(self):
        return self.name


class Msgs(models.Model):
    sender = models.ForeignKey(User, null=True, related_name="sender")
    receiver = models.ForeignKey(User, null=True, related_name="receiver")
    content = models.TextField()

