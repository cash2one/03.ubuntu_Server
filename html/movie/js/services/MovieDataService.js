/**
 * Created by admini on 16-12-16.
 */
app.factory('moviedataservice',['$http','$q','$resource',function ($http,$q,$resource) {

    root = "http://localhost:5002"

    var service = {
        list_datas:[],
        
        req_new_update_list:function (maxnum) {
            var deferred = $q.defer(); // 声明延后执行，表示要去监控后面的执行

            url = root + '/movies/new_update_movies/'+maxnum
            console.log(url)
            $http.get(url).success(function(data,status,headers,config){
                console.log(data)
                deferred.resolve(data);  // 声明执行成功，即http请求数据成功，可以返回数据了
            }).error(function(data,status,headers,config){
                console.error(status)
                deferred.reject(data);   // 声明执行失败，即服务器返回错误
            })

            return deferred.promise;   // 返回承诺，这里并不是最终数据，而是访问最终数据的API

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

        req_links:function(id) {
            var deferred = $q.defer(); // 声明延后执行，表示要去监控后面的执行
            url = root + '/movies/link/'+id
            console.log(url)
            $http.get(url).success(function(data,status,headers,config){
                console.log(data)
                deferred.resolve(data);  // 声明执行成功，即http请求数据成功，可以返回数据了
            }).error(function(data,status,headers,config){
                console.error(status)
                deferred.reject(data);   // 声明执行失败，即服务器返回错误
            })

            return deferred.promise;   // 返回承诺，这里并不是最终数据，而是访问最终数据的API
        },

    }
    return service;
}]);