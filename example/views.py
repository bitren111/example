from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import get_template
import datetime


def hello(request):
    return HttpResponse('Hello world')


def goodbye(request):
    return HttpResponse('Goodbye')


def my_homepage_view(request):
    return HttpResponse('welcome!!!')


def current_time(request):
    now = datetime.datetime.now()
    # t = get_template('current_date.html')
    # html = t.render({'current_date': now})

    return render(request, 'current_datetime.html',
                  {'current_date': now})  # HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s" % (offset, dt)
    return HttpResponse(html)
