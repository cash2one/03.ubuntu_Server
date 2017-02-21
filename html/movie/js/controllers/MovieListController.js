/**
 * Created by admini on 16-12-16.
 */

app.controller('MovieListController', function ($scope, $http, $routeParams, moviedataservice) {
    console.log("MovieListController")
    $scope.links = []


    $scope.initList = function () {

        if ($routeParams.action == "new_update") {
            moviedataservice.req_new_update_list().then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['current']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "year") {
            moviedataservice.req_year_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['current']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "cate") {
            moviedataservice.req_cate_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['current']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }
        else if ($routeParams.action == "search") {
            moviedataservice.req_search_list($routeParams.param).then(function (data) {
                $scope.list_datas = data['data']
                $scope.page_num = data['page']
                $scope.current = data['current']
                $scope.init_page();
            }, function (data) {
                $scope.list_datas = []
            });
        }


    };

    $scope.req_page = function(index) {
        console.log('req_page' + index)
        moviedataservice.set_param(index,28);
        $scope.initList()
    };


    $scope.init_page = function() {



        var txt = "";

        if ($scope.page_num > 1) {

            //// 上一页
            //if ($scope.current == 1) {
            //    txt = "<li class='disabled'><a href='#'>&laquo;</a></li>";
            //}
            //
            //else {
            //    txt = "<li><a href='#'>&laquo;</a></li>";
            //}


            for (var i = 1; i < $scope.page_num + 1; i++) {
                if ($scope.current == i) {
                    txt = txt + "<li class='active'' ><a>" + i + "</a></li>";
                }
                else {
                    txt = txt + "<li><a>" + i + "</a></li>";
                }
            }

            //// 下一页
            //if ($scope.current == $scope.page_num) {
            //    txt = txt + " <li class='disabled'><a href='#'>&raquo;</a></li>";
            //}
            //else {
            //    txt = txt + " <li><a href='#'>&raquo;</a></li>";
            //}

            $('#page').append(txt);
        }
    };
    $('#page li').click(function(){
       console.log("ssss")
    });

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

        //loading参数
        var opts = {
            lines: 12 // The number of lines to draw
            , length: 6 // The length of each line
            , width: 6 // The line thickness
            , radius: 10 // The radius of the inner circle
            , scale: 1 // Scales overall size of the spinner
            , corners: 1 // Corner roundness (0..1)
            , color: '#333' // #rgb or #rrggbb or array of colors
            , opacity: 0.25 // Opacity of the lines
            , rotate: 0 // The rotation offset
            , direction: 1 // 1: clockwise, -1: counterclockwise
            , speed: 1 // Rounds per second
            , trail: 48 // Afterglow percentage
            , fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
            , zIndex: 99999 // The z-index (defaults to 2000000000)
            , className: 'spinner' // The CSS class to assign to the spinner
            , top: '50%' // Top position relative to parent
            , right: '50%' // Left position relative to parent
            , shadow: false // Whether to render a shadow
            , hwaccel: false // Whether to use hardware acceleration
            , position: 'absolute' // Element positioning
        };

        var target = $("#image" + index)

        var spinner = new Spinner(opts).spin(target);

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
            spinner.stop();
            $("#image" + index).append(data);
        }, function (data) {
            $("#image" + index).append(data);
        })
    };


});
