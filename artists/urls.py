from django.conf.urls.defaults import *

urlpatterns = patterns('artists.views',
    ('^$','artists'),
    ('^(?P<object_slug>\w+)/$','artist'),
)

