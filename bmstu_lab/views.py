from django.shortcuts import render, redirect
from bmstu_lab.models import Event
from bmstu_lab.models import Ticket


def DeleteEvent(request,id):
    tickets = Ticket.objects.filter(id_event=id)
    for ticket in tickets:
        ticket.delete()
    events = Event.objects.get(id_event=id)
    events.delete()
    return redirect('/')


def GetEvents(request):
    return render(request, 'events.html', {'data': {
        'events': Event.objects.all()
    }})


def GetEvent(request, id):
    return render(request, 'event.html', {'data': Event.objects.filter(id_event=id)[0]})

