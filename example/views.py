from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse('Hello world')


def goodbye(request):
    return HttpResponse('Goodbye')


def my_homepage_view(request):
    return HttpResponse('welcome!!!')


def current_time(request):
    now = datetime.datetime.now()
    html = 'It is now %s' % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s" % (offset, dt)
    return HttpResponse(html)
