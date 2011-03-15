from django.db import models

from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    description = models.TextField(blank=True)

    website = models.URLField(blank=True)
    email   = models.EmailField(blank=True)
    phone   = models.CharField(max_length=200,blank=True)

    members = models.ManyToManyField(User,blank=True)

    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/vj/%s/' % self.slug

    class Meta:
        ordering=('name',)
