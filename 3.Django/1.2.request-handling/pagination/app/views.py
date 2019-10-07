from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv

#
def index(request):
    return redirect(reverse(bus_stations))


with open(settings.BUS_STATION_CSV) as f:
    csv_data = csv.DictReader(f)
    stations = [row for row in csv_data]


def bus_stations(request):
    main_url = reverse('bus_stations')

    paginator = Paginator([row for row in stations], 10)
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    articles = paginator.get_page(current_page)
    data = articles.object_list

    previous_page_url, next_page_url = None, None
    if articles.has_previous():
        previous_page_url = main_url + f'?page={articles.previous_page_number()}'
    if articles.has_next():
        next_page_url = main_url + f'?page={articles.next_page_number()}'

    return render_to_response('index.html', context={
        'bus_stations': data,
        'current_page': articles.number if articles.number < current_page else current_page,
        'prev_page_url': previous_page_url,
        'next_page_url': next_page_url,
    })
