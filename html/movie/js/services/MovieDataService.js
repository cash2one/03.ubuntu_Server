/**
 * Created by admini on 16-12-16.
 */
app.factory('moviedataservice',['$http','$q','$resource',function ($http,$q,$resource) {

    //root = "http://x2020.top/v1"
    root = "http://localhost:5002"


    req_get = function(path) {
        var deferred = $q.defer(); // 声明延后执行，表示要去监控后面的执行
        url = root + path
        console.log(url)
        $http.get(url).success(function(data,status,headers,config){
            console.log(data)
            deferred.resolve(data);  // 声明执行成功，即http请求数据成功，可以返回数据了
        }).error(function(data,status,headers,config){
            console.error(status)
            deferred.reject(data);   // 声明执行失败，即服务器返回错误
        })

        return deferred.promise;   // 返回承诺，这里并不是最终数据，而是访问最终数据的API
    }

    get_param = function() {
        args = '?page_limit='+ page_limit +'&page_start=' +page_start;
        return args
    }

    page_limit = 28
    page_start = 1

    var service = {

        set_param:function(limit,start){
            page_limit = limit;
            page_start = start;
        },
        clear_param:function(){
          page_limit = 28
            page_start = 1
        },
        req_new_update_list:function() {
            return req_get('/movies/new_update_movies/'+ get_param())
        },

        req_high_rank_list:function() {
            return req_get('/movies/new_movies/'+ get_param())
        },

        req_cate_list:function (cate) {
            return req_get('/movies/cate/' + cate + get_param())
        },

        req_search_list:function(name) {
            return req_get('/movies/name/'+name + get_param())
        },

        req_year_list:function (year) {
            return req_get('/movies/year/' + year + get_param())
        },
        
        req_downloaded_list:function () {
            return req_get('/movies/download/'+get_param())
        },


        req_start_download:function(linkid) {
            return req_get('/movies/'+linkid+'/download/')
        },
        req_links:function(id) {
            return req_get('/movies/link/'+id)
        },
        req_detail:function(id) {
            return req_get('/movies/detail/' + id)
        },

        req_years:function(){
            return req_get('/movies/years/')
        },


    }
    return service;
}]);