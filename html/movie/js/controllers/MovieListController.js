/**
 * Created by admini on 16-12-16.
 */

app.controller('MovieListController', function($scope, $http,moviedataservice) {
    console.log("MovieListController")
    $scope.links = []
    list_datas = moviedataservice.req_new_update_list(10)
    console.log(list_datas)
        //
    //$scope.init_list = function() {
    //    $scope.show_list = false;
    //    // 初始化
    //    //url = 'http://localhost:5002/movies/new_update_movies/'
    //    url = 'http://x2020.top/v1/movies/new_update_movies/'
    //    // 获取电影列表
    //    $http.get(url)
    //        .success(function(response) {
    //            //console.log(response)
    //            $scope.new_movie_list_data = response;
    //            $scope.show_list = true;
    //        })
    //        .error(function(response) {
    //            console.error("request error!" + url)
    //        });
    //
    //}

    //$scope.init_item = function(index,id) {
    //    //url = 'http://localhost:5002/movies/link/'+id
    //    url = 'http://x2020.top/v1/movies/link/' + id
    //    $http.get(url)
    //        .success(function(response) {
    //
    //            $scope.links = $scope.links.concat(response)
    //            //console.log(response)
    //        })
    //        .error(function(response) {
    //            console.error("request error!" + url)
    //        })
    //
    //}
    //
    //$scope.links_data = function(id) {
    //    links = []
    //    for(index in $scope.links) {
    //        if ($scope.links[index].movie == id) {
    //            links.push($scope.links[index])
    //        }
    //    }
    //    return links
    //}
    //
    //
    //$scope.onItemClick = function(url) {
    //    console.log(url)
    //
    //}
});
