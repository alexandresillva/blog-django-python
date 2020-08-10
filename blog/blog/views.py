from django.http import HttpResponse


def hello_world(requeste):
    return HttpResponse("Hello World")
