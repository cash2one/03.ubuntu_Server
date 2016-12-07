/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */

var app = angular.module('movieApp', []);

app.controller('siteCtrl', function($scope, $http) {
    url = 'http://localhost:5002/movies/new_update_movies/'
    url = 'http://x2020.top/v1/movies/new_update_movies/'
    $http.get(url)
        .success(function(response) {
            console.log(response)
            $scope.new_movie_list_data = response;
        })
        .error(function(response) {
           console.error("request error!")
        });

    $scope.onItemClick = function(index) {
        console.log(index)
    }
});
