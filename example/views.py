from django.shortcuts import render
from time import sleep
from .tasks import do_some_expensive_things


def index(request):
    do_some_expensive_things.delay(20)
    return render(request, 'example/index.html')


