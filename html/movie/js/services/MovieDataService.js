/**
 * Created by admini on 16-12-16.
 */
app.factory('moviedataservice',['$http','$q','$resource',function ($http,$q,$resource) {
    var service = {
        listdata:[],

        req_new_update_list:function (maxnum) {
            console.log('req_new_update_list');
            url = 'http://x2020.top/v1/movies/new_update_movies/:num'
            var new_update_movies = $resource(url,{num:'@maxnum'},function (resp) {
                console.log(resp)
            },function (err) {
                console.error("no data!!!")
            });
        },

        req_high_rank_list:function (maxnum) {

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