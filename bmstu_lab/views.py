from django.shortcuts import render
from bmstu_lab.models import Event
from bmstu_lab.models import Ticket
from bmstu_lab.models import User

def GetEvents(request):
    return render(request, 'events.html', {'data': {
        'events': Event.objects.all()
    }})


def GetEvent(request, id):
    return render(request, 'event.html', {'data': Event.objects.filter(id_event=id)[0]})


