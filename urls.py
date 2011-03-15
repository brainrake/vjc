from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blog.views.index', {'template':'index.html'}),
    (r'^blog/', include('blog.urls')),


    #(r'^artists/', include('artists.urls')),
    #(r'^projects/', include('projects.urls')),
    
    
    (r'^booking/', include('booking.urls')),
    #~ (r'^events/', include('events.urls')),
    #~ (r'^inventory/', include('inventory.urls')),
#~ 
    #~ 
    #~ (r'^comments/', include('django.contrib.comments.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'media/'}),

)
