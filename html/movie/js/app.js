/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */

var app = angular.module('movieApp', []);

app.controller('IndexSiteCtrl', function($scope, $http) {

    // 初始化
    //url = 'http://localhost:5002/movies/new_update_movies/'
    url = 'http://x2020.top/v1/movies/new_update_movies/'
    // 获取电影列表
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
