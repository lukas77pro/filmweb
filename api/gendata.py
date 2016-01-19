from .models import *
from datetime import *
from django.http import HttpResponse

def generate(request):
    Film.objects.all().delete()
    Gatunek.objects.all().delete()
    Kraj.objects.all().delete()
    Osoba.objects.all().delete()


    # GATUNKI ======================
    gatunek = Gatunek(nazwa = "Komedia")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Dramat")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Horror")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Akcja")
    gatunek.save()
    gatunek = Gatunek(nazwa = "Sci-Fi")
    gatunek.save()
    # ===============================

    # KRAJE =========================
    kraj = Kraj(nazwa = "Polska")
    kraj.save()
    kraj = Kraj(nazwa = "USA")
    kraj.save()
    kraj = Kraj(nazwa = "Liban")
    kraj.save()
    kraj = Kraj(nazwa = "Australia")
    kraj.save()
    kraj = Kraj(nazwa = "Austria")
    kraj.save()
    kraj = Kraj(nazwa = "Francja")
    kraj.save()
    kraj = Kraj(nazwa = "Hiszpania")
    kraj.save()
    # ===============================

    # FILMY ======================== # manyToMany: produkcja , gatunki
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

    film = Film(
    nazwa = "Matrix",
    nazwa_oryginalna = "The Matrix",
    czas_trwania = 136,
    rok_produkcji = 1999,
    data_premiery = date(1999, 8, 13),
    data_premiery_polska = date(2000, 3, 31),
    budzet = 463517233,
    opis = "Haker komputerowy Neo dowiaduje się od tajemniczych ",
    ocena = 7.6,
    ilosc_ocen = 213122)
    film.save()

    film = Film(
    nazwa = "Pan i władca: Na krańcu świataPan i władca: Na krańcu świata",
    nazwa_oryginalna = "Master and Commander: The Far Side of the World",
    czas_trwania = 138,
    rok_produkcji = 2003,
    data_premiery = date(2003, 11, 14),
    data_premiery_polska = date(2003, 11, 18),
    budzet = 212011111,
    opis = "zasy wojen napoleońskich. Komandor brytyjskiej marynarki ",
    ocena = 7.2,
    ilosc_ocen = 323122)
    film.save()
    # ==============================

    # OSOBY ======================== # relajce
    osoba = Osoba(
    imie = "Clinton",
    nazwisko = "Eastwood",
    data_urodzenia = date(1930, 5, 31),
    data_smierci = None,
    biografia = "Clint Eastwood urodzil sie blalalal",
    kraj_urodzenia = Kraj.objects.filter(nazwa__iexact = "USA").get(),
    wzrost = 193,
    ocena = 8.7,
    ilosc_ocen = 17586)
    osoba.save()

    osoba = Osoba(
    imie = "Peter Lindsay",
    nazwisko = "Weir",
    data_urodzenia = date(1944, 8, 18),
    data_smierci = None,
    biografia = "Najczęściej krytycy określają go mianem - mag, mistyk",
    kraj_urodzenia = Kraj.objects.filter(nazwa__iexact = "Australia").get(),
    wzrost = None,
    ocena = 8.2,
    ilosc_ocen = 2222)
    osoba.save()

    osoba = Osoba(
    imie = "Keanu Charles",
    nazwisko = "Reeves",
    data_urodzenia = date(1964, 9, 2),
    data_smierci = None,
    biografia = "Mówi o sobie, że jest zwykłym chłopakiem bez ojc",
    kraj_urodzenia = Kraj.objects.filter(nazwa__iexact = "Liban").get(),
    wzrost = 185,
    ocena = 7.9,
    ilosc_ocen = 5555743)
    osoba.save()
    # ==============================

    # g1 = Gatunek.objects.filter(nazwa__icontains = "ror").get()
    # g2 = Gatunek.objects.filter(nazwa__icontains = "med").get()

    # f = Film.objects.filter(nazwa__icontains =  "jaZdA").get()
    # f.gatunki.add(g1, g2)


    return HttpResponse("Wygenerowane przykładowe dane!")