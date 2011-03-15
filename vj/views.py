from django.template import RequestContext
from django.shortcuts import *
import datetime

from models import *

def teams(request):
    teams = Team.objects.all()
    return render_to_response('vj/team_list.html',{'object_list':teams},context_instance=RequestContext(request))

def team(request,object_slug):
    team=get_object_or_404(team,slug=object_slug)
    return render_to_response('vj/team_detail.html',{'team':team},context_instance=RequestContext(request))

def team_create(request):
    team=get_object_or_404(team,pk=object_id)
    return render_to_response('vj/team_detail.html',{'team':team},context_instance=RequestContext(request))

def team_update(request):
    team=get_object_or_404(team,pk=object_id)
    return render_to_response('vj/team_detail.html',{'team':team},context_instance=RequestContext(request))
