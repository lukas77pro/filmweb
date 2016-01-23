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
    name = request.GET.get('name', '')  # pobranie parametru .../film?name=... domyslna wartosc -> ''
    count = request.GET.get('count', '')   # pobranie parametru .../film?count=... domyslna wartosc -> ''
    order_by = request.GET.get('order_by', '')   # pobranie parametru .../film?orderby=... domyslna wartosc -> ''
    direction = request.GET.get('direction', 'asc')   # pobranie parametru .../film?orderby=... domyslna wartosc -> ''

    if order_by:
        if direction == 'desc':
            order_by = '-' + order_by
        filmy = Film.objects.order_by(order_by)
    else:
        filmy = Film.objects.all()

    if name:    # wyszukiwanie wg nazwy
        filmy_zgodne = []
        for film in filmy:  # wyszukiwanie jesli nazwa zaczyna się na name
            found = False
            for partname in film.nazwa.split(): # przeszukaj kazdy fragmetn tytulu
                if partname.lower().startswith(name.lower()):
                    filmy_zgodne.append(film)
                    found = True
                    break

            if not found:   # przeszukaj kazdy fragmetn tytulu oryginalnego
                for partname in film.nazwa_oryginalna.split():
                    if partname.lower().startswith(name.lower()):
                        filmy_zgodne.append(film)
                        found = True
                        break

        filmy = filmy_zgodne

    if count:   # zwrocene okreslonej ilosci filmow
        filmy = filmy[:int(count)]

    filmy_ser = serializers.serialize('json', filmy)    # serializacja do json, zwraca string
    data = json.loads(filmy_ser)    # zamienia string na jsona
    return HttpResponse(json.dumps(data))


def film_post(request): # Zapisz silm
    filmData = json.loads(request.body.decode('utf-8'))
    print(filmData)

    nowyFilm = Film()
    nowyFilm.nazwa                  = filmData['nazwa']
    nowyFilm.nazwa_oryginalna       = filmData['nazwa_oryginalna']
    nowyFilm.czas_trwania           = filmData['czas_trwania']
    nowyFilm.rok_produkcji          = filmData['rok_produkcji']
    nowyFilm.budzet                 = filmData['budzet']
    nowyFilm.opis                   = filmData['opis']
    nowyFilm.data_premiery          = convertFromJsonToDate(filmData['data_premiery'])
    nowyFilm.data_premiery_polska   = convertFromJsonToDate(filmData['data_premiery_polska'])
    nowyFilm.save()

    for g in filmData['gatunki']:
        gatunek = Gatunek.objects.get(pk=g['id'])
        nowyFilm.gatunki.add(gatunek)

    for k in filmData['produkcja']:
        kraj = Kraj.objects.get(pk=k['id'])
        nowyFilm.produkcja.add(kraj)

    return HttpResponse("OK")


def convertFromJsonToDate(json):
    if (json is not None):
        date_str = json.split('-')
        date_valid = date(
                int(date_str[0]),
                int(date_str[1]),
                int(date_str[2][:2]))
        date_valid = date_valid + timedelta(days=1)
        return date_valid
    return None


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
