from django.conf.urls.defaults import *

urlpatterns = patterns('booking.views',
    (r'^new/$', 'booking_new'),
)
