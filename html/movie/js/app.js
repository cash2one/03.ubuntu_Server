/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */

$(document).ready(function(){

    app.init()

    $('#datatable-keytable').bootstrapTable({

        columns: [{
            field: 'name',
            title: '名称'
        }, {
            field: 'cate',
            title: '类别'
        }, {
            field: 'sourceurl',
            title: '下载',
            formatter:function(value,row,index) {
                var e = '<button type="button" class="btn btn-primary btn-sm">下载</button>'
                return e
            }
        }, {
            field: 'sourceurl',
            title: '播放',
            formatter:function(value,row,index) {
                var e = '<button type="button" class="btn btn-primary btn-sm">播放</button>'
                return e;
            }
        }],

        onClickCell:function(field, value, row, $element) {
            $.ajax({
                type: "GET",
                url: 'http://x2020.top/v1/localpaths/' + row.id,
                //url: 'http://localhost:5002/localpaths/' + row.id,
                dataType: 'json',
                // response中，包含了 Access-Control-Allow-Origin 这个header，并且它的值里有我们自己的域名时，浏览器才允许我们拿到它页面的数据进行下一步处理。
                success: function (data) {
                    console.log(data)
                }
            })
        },

        rowStyle:function(row,index) {
            var strclass = "";
            if(row.sourceurl == null) {
                strclass = 'danger';
            }
            else if (row.downloadpath == null) {
                strclass = '';
            }
            else if (row.playpath == null) {
                strclass = 'info'
            }
            else {
                strclass = 'success'
            }
            return { classes: strclass }
        },

        data: []



    });

    $("button").click(function() {

        key = $("input:text").val()
        if (key != "") {

            $('#datatable-keytable').bootstrapTable('showLoading');
            $.ajax({
                type: "GET",
                url: 'http://x2020.top/v1/movies/' + key,
                //url: 'http://localhost:5002/movies/' + key,
                dataType: 'json',

                // response中，包含了 Access-Control-Allow-Origin 这个header，并且它的值里有我们自己的域名时，浏览器才允许我们拿到它页面的数据进行下一步处理。
                success: function (data) {

                    var json = eval(data); //数组
                    console.log(json)
                    $('#datatable-keytable').bootstrapTable('hideLoading');
                    $('#datatable-keytable').bootstrapTable('load', json);


                },
                error: function(data) {
                    $('#datatable-keytable').bootstrapTable('hideLoading');
                }
            })

        }
    });
});


//
//$('#table').bootstrapTable({
//    url: 'http://localhost:5002/movies/2',
//    columns: [{
//        field: 'id',
//        title: 'Item ID'
//    }, {
//        field: 'name',
//        title: 'Item Name'
//    }, ]
//});