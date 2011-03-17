from django.template import RequestContext
from django.shortcuts import *
import datetime

from models import *

def artists(request):
    artists = Artist.objects.all()
    return render_to_response('artists/artist_list.html',{'artist_list':artists},context_instance=RequestContext(request))

def artist(request,object_slug):
    artist = get_object_or_404(Artist, slug=object_slug)
    return render_to_response('artists/artist_detail.html',{'artist':artist},context_instance=RequestContext(request))

