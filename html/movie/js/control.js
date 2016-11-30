/**
 * Created by xuqi on 16/11/29.
 */
var app = {

    'init' : function(){

        // item的模板
        var item_transform = {'<>':'div','class':'col-sm-6 col-md-3','html':[{
            '<>':'div','class':'thumbnail','html':[
                {
                    '<>':'img','src':'${img}?x-oss-process=image/resize,m_fill,h_370,w_250','alt':'通用的占位符缩略图'
                },
                {
                    '<>':'div','class':'caption','html':[
                    {
                        '<>':'p','class':'cut','html':'${name}',
                    },
                    {
                        '<>':'p','html':[
                        {
                            '<>':'a','href':'${sourceurl}','class':'btn btn-primary', 'role':'button', 'html':'下载地址'
                        },
                        {
                            '<>':'a','href':'${url}','class':'btn btn-primary', 'role':'button', 'html':'详细地址'
                        },
                    ]
                    },
                ]
                },
            ]
        }
        ]
        };

        $.ajax({
            type: "GET",
            url: 'http://x2020.top/v1/movies/',
            //url:'http://localhost:5002/movies/',
            dataType: 'json',
            success: function (data) {
                var json = eval(data); //数组
                context = ""
                for (index in json) {
                    console.log(json[index])

                    context += json2html.transform(json[index],item_transform)
                }
                $('#list').html(context)
            },
            error: function(data) {
                console.error("没有数据")
                return {}
            }
        })

    },


}