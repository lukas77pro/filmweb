var app = angular.module('app', []);
app.controller('controller', function($scope, $http) {

    $scope.loadCountries = function() {
        $scope.countries = []
        $http({
          method: 'GET',
          url: '/api/countries'
        }).then(function successCallback(response) {
            c = response.data
            for (var i = 0; i < c.length; i++) {
                $scope.countries.push(c[i].fields.nazwa)
            }
            console.log(response)
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
            c = response.data
            for (var i = 0; i < c.length; i++) {
                $scope.genres.push(c[i].fields.nazwa)
            }
            console.log(response)
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
            c = response.data
            for (var i = 0; i < c.length; i++) {
                $scope.professions.push(c[i].fields.nazwa)
            }
            console.log(response)
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
        $scope.searchfilm = {
            name : '',
            films : []
        }
    };

    $scope.init();

});