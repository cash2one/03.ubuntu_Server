/**
 * Created by admini on 16-12-16.
 */
app.factory('moviedata',['$http','$q',function ($http,$q) {
    var service = {
        listdata:[],
        
        req_new_update_list:function (maxnum) {

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