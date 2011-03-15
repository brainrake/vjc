from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Item(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200,blank=True)
    notes = models.TextField(blank=True)
    code = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.name


class Rental(models.Model):
    item = models.ForeignKey(Item)

    planned_date_out = models.DateTimeField()
    planned_date_in = models.DateTimeField()
    date_out = models.DateTimeField(null=True,blank=True)
    date_in = models.DateTimeField(null=True,blank=True)
    
    user = models.ForeignKey(User,null=True,blank=True)
    contact = models.CharField(max_length=200,blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.item)
