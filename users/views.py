from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def profile(requst):
    context = {
        "name": "haco",
        "age": 25,
        "height": 160,
        "weight": 51,
    }
    return JsonResponse(context)
