/**
 * Created by admini on 16-12-16.
 */

app.controller('MovieListController', function($scope, $http,$routeParams,moviedataservice) {
    console.log("MovieListController")
    $scope.links = []

    $scope.initList  = function(){
        if ($routeParams.action == "new_update"){
            moviedataservice.req_new_update_list().then(function(data) {
                $scope.list_datas = data
            },function(data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "year"){
            moviedataservice.req_year_list($routeParams.param).then(function(data) {
                $scope.list_datas = data
            },function(data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "cate"){
            moviedataservice.req_cate_list($routeParams.param).then(function(data) {
                $scope.list_datas = data
            },function(data) {
                $scope.list_datas = []
            });
        }
    }

    $scope.download = function(url,linkid){
        moviedataservice.req_start_download(linkid).then(function(data){

        },function(data) {

        });
    };

    $scope.play = function(url,linkid) {
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
