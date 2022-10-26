from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS = (
        (1, 'admin'),  # admin
        (2, 'users'),  # user
    )
    type = models.IntegerField(choices=STATUS, default=2)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

class Information(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/')
    description = models.TextField()
    googleplay = models.CharField(max_length=255)
    appstore = models.CharField(max_length=255)


class AdImage(models.Model):
    photo = models.ImageField(upload_to='media/')


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/')


class Region(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ads(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    photo = models.ManyToManyField(AdImage)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    status = models.IntegerField(choices=(
        (1, 'in admin'),
        (2, 'accepted'),
        (3, 'rejected'),
        (4, 'sold'),
    ), default=1)
    is_top = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=True)
    

