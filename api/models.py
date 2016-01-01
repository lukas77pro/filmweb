from django.db import models


class Zawod(models.Model): # v
    nazwa = models.CharField(max_length=50) # Nazwa zawodu: 'aktor', 'reżyser' ...


class Gatunek(models.Model): # v
    nazwa = models.CharField(max_length=50) # Nazwa gatunku: 'komedia', 'dramat' ...


class Kraj(models.Model): # v
    nazwa = models.CharField(max_length=50) # Nazwa kraju: 'Polska', 'Węgry' ...


class Nagroda(models.Model): # v
    nazwa = models.CharField(max_length=50) # Nazwa nagrody: 'Oscar', 'Złote coś tam' ...
    opis = models.TextField(blank=True) # Opis nagrody: 'Nagroda nadawna za coś tam' ...


class Kategoria_nagrody(models.Model): # v
    kategoria = models.CharField(max_length=100) # Kategoria nagrody: 'Za najlepszą rolę drugoplanową' ...
    nagroda = models.ForeignKey(Nagroda, on_delete=models.CASCADE)


class Film(models.Model): # v
    nazwa = models.CharField(max_length=100) # Nazwa flmu: 'Ale jazda!', 'Waleczne serce' ...
    nazwa_oryginalna = models.CharField(max_length=100) # Nazwa flmu: 'Interstate 60', 'Braveheart' ...
    czas_trwania = models.PositiveIntegerField(null=True)
    rok_produkcji = models.PositiveIntegerField(null=True)
    data_premiery = models.DateField(null=True)
    data_premiery_polska = models.DateField(null=True)
    budzet = models.PositiveIntegerField(null=True)
    opis = models.TextField(blank=True)
    ocena = models.FloatField(default=0.0) # Ocena srednia: '5.0'
    ilosc_ocen = models.PositiveIntegerField(default=0) # Ilosc głosujących: '30'
    produkcja = models.ManyToManyField(Kraj)
    gatunki = models.ManyToManyField(Gatunek)


class Osoba(models.Model): # v
    imie = models.CharField(max_length=50)  # Imie: 'Janusz', 'Jan Maria'
    nazwisko = models.CharField(max_length=50) # Nazwisko: 'Filipiak', 'Rokita'
    data_urodzenia = models.DateField(null=True, blank=True)
    data_smierci = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)
    wzrost = models.IntegerField(null=True, blank=True)
    kraj_urodzenia = models.ForeignKey(Kraj, null=True)
    ocena = models.FloatField(default=0.0) # Ocena srednia: '5.0'
    ilosc_ocen = models.PositiveIntegerField(default=0) # Ilosc głosujących: '30'


class Recenzja(models.Model): # v
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, null=True)
    recenzja = models.TextField


class Rola(models.Model): # v
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    zawod = models.ForeignKey(Zawod, on_delete=models.CASCADE)
    ocena = models.FloatField(default=0.0) # Ocena srednia: '5.0'
    ilosc_ocen = models.PositiveIntegerField(default=0) # Ilosc głosujących: '30'


class Nagroda_rozdana(models.Model): # v
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)
    nagroda = models.ForeignKey(Nagroda, on_delete=models.CASCADE)
    kategoria = models.ForeignKey(Kategoria_nagrody, on_delete=models.CASCADE, null=True)
    data_wydania = models.DateField(null=True)