from .models import *
from datetime import *
from json import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, SimpleCookie
from django.core import serializers
import json

def user(request):
    print('user')
    pass


@csrf_exempt
def film(request):

    methods = {
        "GET" : film_get,
        "POST" : film_post,
    }
    method = methods.get(request.method)

    return method(request)

def film_get(request): # Wszystkie filmy
    filmy = Film.objects.all()
    filmy_ser = serializers.serialize('json', filmy)
    data = json.loads(filmy_ser)
    return HttpResponse(json.dumps(data))


def film_post(request):
    return HttpResponse("KurwaPOST")



def countries(request):
    kraje = Kraj.objects.all()
    kraje_ser = serializers.serialize('json', kraje)
    data = json.loads(kraje_ser)
    return HttpResponse(json.dumps(data))

def genres(request):
    gatunek = Gatunek.objects.all()
    gatunek_ser = serializers.serialize('json', gatunek)
    data = json.loads(gatunek_ser)
    return HttpResponse(json.dumps(data))

def professions(request):
    zawod = Zawod.objects.all()
    zawod_ser = serializers.serialize('json', zawod)
    data = json.loads(zawod_ser)
    return HttpResponse(json.dumps(data))

# @csrf_exempt
# def film(request):
#     if request.method == 'POST':
#         user = Uzytkownik()
#         fixdata = ((request.body).decode('utf-8'))
#         data = loads(fixdata)
#
#         user.login = data['login']
#         user.haslo = data['haslo']
#         user.email = data['email']
#         if 'imie' in data:
#             user.imie = data['imie']
#         if 'nazwisko' in data:
#             user.nazwisko = data['nazwisko']
#         user.save()
#
#         return HttpResponse(dumps(data), content_type="application/json")
#
#     return HttpResponse("User request error!")