import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Main page': reverse('home'),
        'Show current time': reverse('time'),
        'Show content of work directory': reverse('workdir')
    }

    context = {
        'pages': pages
    }

    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Current time: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    return HttpResponse('<br>'.join(os.listdir(path='.')))