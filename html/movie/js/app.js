/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */

'use strict';

var app= angular.module('movieApp', ['ngResource', 'ngRoute'])
    .config(function($routeProvider){
        $routeProvider.when('/list/:action/:param',{

            templateUrl:'view/MovieList.html',
           // controller: 'MovieListController'

        });

        $routeProvider.when('/downloaded_list/',{

            templateUrl:'view/DownloadList.html',
            //controller: 'DownloadListController'
        });

        $routeProvider.when('/search_list/:key',{

            templateUrl:'view/MovieList.html',
            //controller: 'EventController'
        });

        $routeProvider.when('/cate_list/:maxnum',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });


        $routeProvider.when('/movies/year/:year',{

            templateUrl:'view/MovieList.html',
           // controller: 'EventController'
        });







        $routeProvider.otherwise({redirectTo:'/list/:action/:num'});

        console.log('App called.');
    });