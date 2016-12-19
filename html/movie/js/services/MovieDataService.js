/**
 * Created by admini on 16-12-16.
 */
app.factory('moviedataservice',['$http','$q','$resource',function ($http,$q,$resource) {

    root = "http://localhost:5002"
    var service = {
        list_datas:[],
        
        req_new_update_list:function (maxnum) {
            url = root + '/movies/new_update_movies/'+maxnum
            $http.get(url).success(function(data,status,headers,config){
                console.log(data)
                return data
            }).error(function(data,status,headers,config){
                console.error(status)
            })

        },

        req_high_rank_list:function (maxnum) {
            url = root + '/movies/new_update_movies/'+maxnum
            $http.get(url).success(function(data,status,headers,config){
                console.log(data)
            }).error(function(data,status,headers,config){

            })
        },

        req_cate_list:function (cate) {

        },
        
        req_new_year_list:function (year) {
            
        },
        
        req_downloaded_list:function () {
            
        },
        
        req_search_list:function (key) {
            
        },


    }
    return service;
}]);