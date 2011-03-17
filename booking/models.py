from django.db import models

from django.contrib.auth.models import User

class BookingRequest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=200)

    description = models.TextField(help_text='technika igeny stb')

    payment = models.PositiveIntegerField(help_text='ft')

    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)


class BookingReply(models.Model):
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)


class Equipment(models.Model):
    TYPE_CHOICES = (( 'projector', 'projector' ),
                    ( 'cable', 'cable' ),
                    ( 'adapter', 'adapter' ),
                    ( 'other', 'other'), )
    
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
