from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.CharField(max_length=50)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-timestamp", "-updated"]


class Portfolio(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True)
    industry = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Employee(models.Model):
    full_name = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True)
    job_title = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    email = models.CharField(max_length=40)


    def __unicode__(self):
        return self.full_name

    def __str__(self):
        return self.full_name
