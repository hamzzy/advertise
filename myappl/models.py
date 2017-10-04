from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    user=models.OneToOneField(User)
    picture=models.FileField(null=True,blank=False,upload_to='media')
    location=models.CharField(max_length=200)

    class Meta:
        ordering=('user',)
        verbose_name='UserProfile'
        verbose_name_plural='usersprofile'

    def __unicode__(self):
        return self.picture


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "category/%s/" % (self.slug)




class Ads(models.Model):
    name=models.CharField(max_length=300)
    text=models.TextField()
    phone=models.CharField(max_length=200)
    price=models.CharField(max_length=200,blank=True)
    picture=models.FileField(null=True,blank=False,upload_to='media')
    location=models.ForeignKey('Location')
    category=models.ForeignKey('Category')
    user=models.ForeignKey(User,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'ads'
        verbose_name_plural = 'ads'
    def __unicode__(self):
        return self.name



class Location(models.Model):
    name=models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


