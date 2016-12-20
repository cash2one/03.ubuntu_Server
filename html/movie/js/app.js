/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */

'use strict';

var app= angular.module('movieApp', ['ngResource', 'ngRoute'])
    .config(function($routeProvider){
        $routeProvider.when('/new_update_list/:maxnum',{

            templateUrl:'view/MovieList.html',
           // controller: 'MovieListController'

        });

        $routeProvider.when('/high_rank_list/:maxnum',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });


        $routeProvider.when('/cate_list/:maxnum',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });


        $routeProvider.when('/new_year_list/:maxnum',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });


        $routeProvider.when('/downloaded_list/:maxnum',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });


        $routeProvider.when('/search_list/:key',{

            templateUrl:'templates/EventDetails.html',
            controller: 'EventController'
        });

        $routeProvider.otherwise({redirectTo:'/search_list/:maxnum'});

        console.log('App called.');
    });