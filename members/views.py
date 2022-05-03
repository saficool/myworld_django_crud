from copyreg import constructor
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import members
from .models import Members
from django.urls import reverse

# Create your views here.


def index(request):
    members = Members.objects.all().values()
    template = loader.get_template('members/myfirst.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('members/add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    _first_name = request.POST['first']
    _last_name = request.POST['last']
    member = Members(first_name=_first_name, last_name=_last_name)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('members/update.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    print("Hi")
    first = request.POST['first']
    last = request.POST['last']

    member = Members.objects.get(id=id)
    member.first_name = first
    member.last_name = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
