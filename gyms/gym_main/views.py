from django.http import HttpResponse


def index(request):
    time = 1
    return HttpResponse(f"Current time: {time}")
