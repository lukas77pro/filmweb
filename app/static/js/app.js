var app = angular.module('app', []);
app.controller('controller', ['$scope', '$http', function($scope, $http) {

    // ========== FACTORY ============
    var createPerson = function() {
        return {
            id : null,
            imie : '',
            nazwisko : '',
            data_urodzenia : null,
            data_smierci : null,
            biografia : '',
            wzrost : null,
            kraj_urodzenia : null,
            ocena : null,
            ilosc_ocen : null
        }
    };


    var createFilm = function() {
        return {
            id : null,
            nazwa : '',
            nazwa_oryginalna : '',
            czas_trwania : null,
            rok_produkcji : null,
            data_premiery : null,
            data_premiery_polska : null,
            budzet : null,
            opis : '',
            ocena : null,
            ilosc_ocen : null,
            produkcja : [],
            gatunki : []
        }
    };

    var createCountry = function() {
        return {
            id : null,
            nazwa : ''
        }
    };

    var createGenre = function() {
        return {
            id : null,
            nazwa : ''
        }
    };

    var createProfession = function() {
        return {
            id : null,
            nazwa : ''
        }
    };
    // ===============================


    // ======= DODAWANIE OSOBY =======
    $scope.addPerson = function() {
        $scope.state = 'personadd'
        $scope.nowaOsoba = createPerson()
    };

    $scope.pushPerson = function() {
        $http({
              method: 'POST',
              url: '/api/person',
              data: $scope.nowaOsoba
        }).then(function successCallback(response) {
            $scope.toggleModal('Sukces!',
                'Dodano osobę do bazy danych!',
                'Powrót do strony głównej',
                $scope.goMain)
        });
    };
    // ===============================


    // ======= DODAWANIE FILMU =======
    $scope.addFilm = function() {
        $scope.state = 'filmadd'
        $scope.nowyFilm = createFilm()
    };

    // DODAWANIE KRAJÓW PRODUKCJI
    $scope.addGenreToNewFilm = function() {
        gatunki = $scope.nowyFilm.gatunki
        szukany = $scope.items.genre
        if (gatunki.indexOf(szukany) == -1) {
            gatunki.push(szukany)
        }
        $scope.items.genre = ''
    };
    $scope.deleteGenreFromNewFilm = function(index) {
        $scope.nowyFilm.gatunki.splice(index, 1)
    };


    // DODAWNIA KRAJÓW PRODUKCJI
    $scope.addCountryToNewFilm = function() {
        kraje = $scope.nowyFilm.produkcja
        szukany = $scope.items.country
        if (kraje.indexOf(szukany) == -1) {
            kraje.push(szukany)
        }
        $scope.items.country = ''
    };
    $scope.deleteCountryFromNewFilm = function(index) {
        $scope.nowyFilm.produkcja.splice(index, 1)
    };

    $scope.validAddFilmForm = function() {
        if ($scope.nowyFilm.gatunki.length > 0 &&
            $scope.nowyFilm.produkcja.length > 0) {
            return true
        }
        return false
    };


    $scope.pushFilm = function() {
        if ($scope.validAddFilmForm()) {
            $http({
              method: 'POST',
              url: '/api/film',
              data: $scope.nowyFilm
            }).then(function successCallback(response) {
                $scope.toggleModal('Sukces!',
                'Dodano film do bazy danych!',
                'Powrót do strony głównej',
                $scope.goMain)
            });
        }
    };


    $scope.info = function(arg) {
        console.log(arg)
    };
    // ===============================

    // DODAWNIA KRAJÓW PRODUKCJI
    $scope.addCountryToNewFilm = function() {
        kraje = $scope.nowyFilm.produkcja
        szukany = $scope.items.country
        if (kraje.indexOf(szukany) == -1) {
            kraje.push(szukany)
        }
        $scope.items.country = ''
    };
    $scope.deleteCountryFromNewFilm = function(index) {
        $scope.nowyFilm.produkcja.splice(index, 1)
    };

    $scope.validAddFilmForm = function() {
        if ($scope.nowyFilm.gatunki.length > 0 &&
            $scope.nowyFilm.produkcja.length > 0) {
            return true
        }
        return false
    };

    $scope.info = function(arg) {
        console.log(arg)
    };
    // ===============================

    $scope.goMain = function() {
        $scope.items = {
            genre : '',
            country : '',
            filmsearch : {
                name : '',
                films : []
            },
            modal : {
                show : false,
                header : '',
                body : '',
                footer : '',
                func : null
            }
        }
        $scope.state = 'main'
    };

    $scope.toggleModal = function(header, body, footer, func) {
        $scope.items.modal.show = true
        $scope.items.modal.header = header
        $scope.items.modal.body = body
        $scope.items.modal.footer = footer
        $scope.items.modal.func = func
    };

    $scope.hideModal = function() {
        $scope.items.modal.show = false
        $scope.items.modal.func()
    };

    $scope.findFilms = function() {
        console.log('witam')
        if ($scope.items.filmsearch.name.length > 1) {
            $scope.loadFilms()
        } else {
            $scope.items.filmsearch.films = []
        }
    };

    $scope.viewFilm = function(index) {
        $scope.state = 'filmview'
        console.log(index)
    };

    // ============ ŁADOWANIE DANYCH ===========
    $scope.loadFilms = function() {
        $scope.items.filmsearch.films = []
        $http({
          method: 'GET',
          url: '/api/film',
          params: {
            name : $scope.items.filmsearch.name,
            order_by : 'ocena',
            direction : 'desc'
          }
        }).then(function successCallback(response) {
            f = response.data
            for (var i = 0; i < f.length; i++) {
                film = createFilm()
                film.id = f[i].pk
                film.nazwa = f[i].fields.nazwa
                film.nazwa_oryginalna = f[i].fields.nazwa_oryginalna
                $scope.items.filmsearch.films.push(film)
            }
            console.log($scope.items.filmsearch.films)
          }, function errorCallback(response) {
            console.log('Load filmss error!')
        })
    };

    $scope.loadCountries = function() {
        $scope.countries = []
        $http({
          method: 'GET',
          url: '/api/countries'
        }).then(function successCallback(response) {
            c = response.data
            for (var i = 0; i < c.length; i++) {
                con = createCountry()
                con.id = c[i].pk
                con.nazwa = c[i].fields.nazwa
                $scope.countries.push(con)
            }
          }, function errorCallback(response) {
            console.log('Load countries error!')
        });
    };

    $scope.loadGenres = function() {
        $scope.genres = []
        $http({
          method: 'GET',
          url: '/api/genres'
        }).then(function successCallback(response) {
            g = response.data
            for (var i = 0; i < g.length; i++) {
                gen = createGenre()
                gen.id = g[i].pk
                gen.nazwa = g[i].fields.nazwa
                $scope.genres.push(gen)
            }
          }, function errorCallback(response) {
            console.log('Load genres error!')
          });
    };

    $scope.loadProfessions = function() {
        $scope.professions = []
        $http({
          method: 'GET',
          url: '/api/professions'
        }).then(function successCallback(response) {
            p = response.data
            for (var i = 0; i < p.length; i++) {
                pro = createProfession()
                pro.id = p[i].pk
                pro.nazwa = p[i].fields.nazwa
                $scope.professions.push(pro)
            }
          }, function errorCallback(response) {
            console.log('Load countries error!')
          });
    };

    $scope.loadData = function() {
        $scope.loadProfessions();
        $scope.loadGenres();
        $scope.loadCountries();
    }
    // ŁADOWANIE DANYCH
    // ==============================================


    $scope.init = function() {
        $scope.loadData()
        $scope.goMain()
    };

    $scope.init();

}]);