from django.conf.urls.defaults import *

urlpatterns = patterns('vj.views',
    ('^$','teams'),
    ('^(?P<object_slug>\w+)/$','team'),
)

