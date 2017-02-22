/**
 * Created by admini on 16-12-16.
 */

app.controller('MovieListController', function ($location,$scope, $http, $routeParams, moviedataservice) {
    console.log("MovieListController")
    $scope.links = []


    $scope.initList = function () {

        if ($location.search().hasOwnProperty('page_start') && $location.search().hasOwnProperty('page_limit'))
        {
            moviedataservice.set_param($location.search().page_limit,$location.search().page_start)
        }
        else {
            moviedataservice.clear_param()
        }

        if ($routeParams.action == "new_update") {
            moviedataservice.req_new_update_list().then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['page_start']
                $scope.page_limit = data['page_limit']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "year") {
            moviedataservice.req_year_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['page_start']
                $scope.page_limit = data['page_limit']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "cate") {
            moviedataservice.req_cate_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['page_start']
                $scope.page_limit = data['page_limit']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "search") {
            moviedataservice.req_search_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['page_start']
                $scope.page_limit = data['page_limit']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }


    };

    $scope.req_page = function(index) {
        console.log('req_page' + index)
        moviedataservice.set_param(28,index);
        $scope.initList()
    };


    $scope.init_page = function() {

        var txt = "";

        $('#page').empty()

        if ($scope.page_num > 1) {

            for (var i = 1; i < $scope.page_num + 1; i++) {
                if ($scope.current == i) {
                    txt = txt + "<li class='active'' ><a>" + i + "</a></li>";
                }
                else {
                    txt = txt + "<li><a href='#" + $location.path() + "?page_limit="+ $scope.page_limit +"&page_start=" + i +"'>" + i + "</a></li>";
                }
            }

            $('#page').append(txt);
        }
    };

    $scope.copylink = function (index) {

        var clipboard = new Clipboard('#btn_cpylink_' + index);

        clipboard.on('success', function (e) {
            console.info('Action:', e.action);
            console.info('Text:', e.text);
            console.info('Trigger:', e.trigger);
            alert("复制成功:" + e.text);
            e.clearSelection();
            //e.clearSelection();
            clipboard.destroy();
        });

        clipboard.on('error', function (e) {
            console.error('Action:', e.action);
            console.error('Trigger:', e.trigger);
        });
    };


    $scope.download = function (url, linkid) {
        moviedataservice.req_start_download(linkid).then(function (data) {

        }, function (data) {

        });
    };

    $scope.play = function (url, linkid) {
        console.log(url)
    };

    $scope.load_detail_info = function (movie, index, url) {

        $scope.load_thumbnail(url);

        // request detail info
        moviedataservice.req_detail(movie).then(function (data) {
            $scope.item_detial = data[0]
            // set info to html
            if (data.length > 0) {
                $('#detail_info' + index).html(data[0].info)

                // load link
                moviedataservice.req_links(movie).then(function (data) {
                    $scope.download_links = data
                }, function (data) {
                    console.log(data)
                });

            }
        }, function (data) {
            console.log(data)
        });
    };

    $scope.getfilename = function (path) {
        var pos1 = path.lastIndexOf('/');
        var pos2 = path.lastIndexOf('\\');
        var pos = Math.max(pos1, pos2)
        if (pos < 0)
            return path;
        else
            return path.substring(pos + 1);
    }

    $scope.loadimage = function (index, url) {


        var surl = url + '?x-oss-process=image/resize,m_fill,h_370,w_250';

        function imgLoadAsync(url) {
            return new Promise(function (resolve, reject) {
                var img = new Image();

                img.onload = function () {
                    resolve(img);
                }

                img.onerror = function () {
                    img.src = "http://x2020-movie.oss-cn-shanghai.aliyuncs.com/NotFind.jpg?x-oss-process=image/resize,m_pad,h_370,w_250,color_ffffff"
                    reject(img);
                }

                img.style = "width: 100%;";
                img.src = url;

            });
        }

        imgLoadAsync(surl).then(function (data) {
            $("#img_span" + index).empty();
            $("#img_span" + index).append(data);
        }, function (data) {
           // $("#image" + index).append(data);
        })
    };

    $scope.load_thumbnail = function(url) {
        console.log(url)
        var surl = url + '?x-oss-process=image/resize,m_fill,h_370,w_250';

        function imgLoadAsync(url) {
            return new Promise(function (resolve, reject) {
                var img = new Image();

                img.onload = function () {
                    resolve(img);
                }
                img.onerror = function () {
                    reject(img);
                }
                img.class= "img-thumbnail";
                img.style= "width: 100%;";
                img.src = url;

            });
        }

        imgLoadAsync(surl).then(function (data) {
            $("#thumbnail_pic").empty();
            $("#thumbnail_pic").append(data);

        }, function (data) {
            // $("#image" + index).append(data);
        })
    };


});
