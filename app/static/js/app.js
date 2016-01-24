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
            console.log('dodano osobe')
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
                console.log('wyslano film')
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


    $scope.pushFilm = function() {
        if ($scope.validAddFilmForm()) {
            $http({
              method: 'POST',
              url: '/api/film',
              data: $scope.nowyFilm
            }).then(function successCallback(response) {
                console.log('wyslano film')
            });
        }
    };


    $scope.info = function(arg) {
        console.log(arg)
    };
    // ===============================

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


    $scope.init = function() {
        $scope.loadData();
        $scope.state = "main"
        /*$scope.searchfilm = {
            name : '',
            films : []
        }*/
    };
    x = createFilm()
    console.log(x);
    $scope.init();

}]);