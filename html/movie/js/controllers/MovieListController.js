/**
 * Created by admini on 16-12-16.
 */

app.controller('MovieListController', function($scope, $http,$routeParams,moviedataservice) {
    console.log("MovieListController")
    $scope.links = []

    $scope.initList  = function(fun){
        if (fun == "new_update_list"){
            moviedataservice.req_new_update_list($routeParams.maxnum).then(function(data) {
                $scope.list_datas = data
            },function(data) {
                $socpe.list_datas = []
            });
        }
    }

    $scope.download = function(url){
       console.log(url)
    };

    $scope.play = function(url) {
        console.log(url)
    };

    $scope.loadlink = function(movie) {
        moviedataservice.req_links(movie).then(function(data) {
            $scope.download_links =data
        },function(data) {
            console.log(data)
        });
    };


});
