from django.template import RequestContext
from django.shortcuts import *
from django.forms import ModelForm

from models import *

class BookingRequestForm(ModelForm):
    class Meta:
        model = BookingRequest

def booking_new(request):
    form = BookingRequestForm(request.POST or None)

    c = RequestContext(request,{
        'form':form
    })
    return render_to_response('booking/booking_form.html',c)
