/**
 * Created by xuqi on 16/11/8.
 */
/**
 * Created by xuqi on 16/11/5.
 */
$(function () {
    'use strict'
})

$(document).ready(function(){

    $('#datatable-keytable').bootstrapTable({

        columns: [{
            field: 'id',
            title: 'Item ID'
        }, {
            field: 'name',
            title: 'Item Name'
        },],

        data: []

    });

    $("button").click(function() {

        key = $("input:text").val()
        console.log(key)
        $('#datatable-keytable').bootstrapTable('showLoading');
        $.ajax({
            type: "GET",
            url: 'http://localhost:5002/movies/' + key,
            dataType: 'json',

            // response中，包含了 Access-Control-Allow-Origin 这个header，并且它的值里有我们自己的域名时，浏览器才允许我们拿到它页面的数据进行下一步处理。
            success: function (data) {

                var json = eval(data); //数组
                $('#datatable-keytable').bootstrapTable('hideLoading');
                $('#datatable-keytable').bootstrapTable('load',json);


            }
        })
    })
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