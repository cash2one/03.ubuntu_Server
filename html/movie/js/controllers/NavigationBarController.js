/**
 * Created by admini on 16-12-16.
 */

app.controller('NavigationController', function($scope,$rootScope, $http,moviedataservice) {
    $scope.init = function(){

        moviedataservice.req_years($routeParams).then(function(data) {
            $scope.list_years = data
        },function(data) {
            $socpe.list_years = []
        });
    }

    $scope.btn_search = function(name){
        redirectTo:'#'
        moviedataservice.req_search_list(name).then(function(data) {
            $socpe.list_datas = data
        },function(data) {
            $socpe.list_datas = []
        });
    }
});