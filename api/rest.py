from .models import *
from datetime import *
from django.http import HttpResponse

def generate(request):
    Film.objects.all().delete()
    Gatunek.objects.all().delete()

    film = Film(
    nazwa = "Ale jazda!",
    nazwa_oryginalna = "Intersate 60",
    czas_trwania = 115,
    rok_produkcji = 2002,
    data_premiery = date(2002, 4, 13),
    data_premiery_polska = date(2003, 1, 26),
    budzet = 12412412,
    opis = "Zajebisty film opowiwada o kolesiu co coś tam....",
    ocena = 5.0,
    ilosc_ocen = 30)
    film.save()

    gatunek = Gatunek(nazwa = "Komedia")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Dramat")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Horror")
    gatunek.save()

    g1 = Gatunek.objects.filter(nazwa__icontains = "ror").get()
    g2 = Gatunek.objects.filter(nazwa__icontains = "med").get()

    f = Film.objects.filter(nazwa__icontains =  "jaZdA").get()
    f.gatunki.add(g1, g2)


    return HttpResponse("Wygenerowane przykladowe dane")


def user(request):
    print('user')
    pass

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