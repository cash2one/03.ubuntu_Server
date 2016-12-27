/**
 * Created by xuqi on 16/12/27.
 */
app.controller('DownloadListController', function($scope, $http,$routeParams,moviedataservice) {
    $scope.links = []

    $scope.initList = function(){
        console.log('DownloadListController initlist')
        moviedataservice.req_downloaded_list().then(function(data) {
            $scope.list_datas = data
        },function(data) {
            $scope.list_datas = []
        });
    }
    $scope.getstatus = function(status) {
        if(status == 'error')
            return 'danger'
        else if (status == '')
            return 'success'
        else if (status == '')
            return 'info'
    }

    $scope.getPer = function(completedLength,totalLength) {
        if (totalLength == '0')
            return "width: 0%"

        return "width: "+ totalLength/completedLength * 100 +"%"

    }
});