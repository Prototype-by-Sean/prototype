var widthChange = function() {
    $('.video').addClass('video_phone');
    $('.status_backers').addClass('status_backers_phone');
    $('.status_backers_sec').addClass('status_backers_sec_phone');
}//判斷解析度版本的公用部分
$(window).resize(function () {
    var width_2 = $(window).width();
    if (width_2 < 600){
        $(width_move());
    }
    if (width_2 > 600){
        $('.video').removeClass('video_phone');
        $('.status_backers').removeClass('status_backers_phone');
        $('.status_backers_sec').removeClass('status_backers_phone');
    }
});//滑鼠縮放事件
var functionDatabase = function(){
    function MonDay(year,month,day){
        var toDay_1 = new Date(year,month,day);//將日期存入變數
        for (i=0;toDay_1.getDay() != 1;i++){//運算到找到禮拜一為止
            var i_2=i*24;//一天24小時
            toDay_1.setHours(day-i_2);//迴圈每跑一次就減去一天
        }
        return toDay_1
    }//輸入日期會找出當周星期一的日期，手輸月分會加一個月，系統用陣列記錄月份
}

$(document).ready( function() {
    var height_1 = $(window).height();//取得視窗取得視窗高度
    var width_2 = $(window).width();   //視窗實際寬度
    if (width_2 < 600){
        $(widthChange());
    }//　切換手機版本
});//主程式
$(document).ready(function(){
    var flag=0,timer,timer_2;//nav使用變數
    $('.logo').hover(function(){
        $('.logo').toggleClass('change');
    });//切換LOGE顏色
    $('.nav').mouseenter(function(){
        clearTimeout(timer_2);
        flag=1;
    });//滑鼠移入ＮＡＶ取消縮回倒數
    $('.nav').mouseleave(function() {
        if ($(document).scrollTop() > 0) {//避免在頂端時縮回
            flag=0;
            timer_2 = setTimeout(function () {
                $('.nav').slideUp(200);
            }, 1000);
        }
    });//滑鼠移出時倒數縮回
    var height_top = $(document).scrollTop(),height_top_2;
    var navSlide = function(){
        if($(document).scrollTop()==0){
            clearTimeout(timer_2);
            $('.nav').addClass('navSlide').slideDown(500);
            setTimeout(function(){flag=0},500);
        }//如果位於頁面頂端，顯示ＮＡＶ
        if(flag==0 || flag==1) {//避免動作重複偵測
            height_top_2 = $(document).scrollTop();
            if (height_top_2 - height_top > 0) {//往下，利用１０毫秒差距的高度偵測往上還是往下
                flag=2;
                $('.nav').slideUp(200);//往上縮回
                setTimeout(function(){
                    flag=0;
                    height_top = $(document).scrollTop();
                },200);//滑動作用期間不偵測滑棒動作
            }
            else if (height_top_2 - height_top < 0 && flag==0) {
                flag=1;
                $('.nav').addClass('navSlide').slideDown(200);
                setTimeout(function(){flag=0
                    height_top = $(document).scrollTop();
                },200);
                clearTimeout(timer_2);//如過滑鼠繼續往上，停止縮回計時
                timer_2=setTimeout(function(){$('.nav').slideUp(200);
                },3000);//閒置時ＮＡＶ３秒縮回
            }//滑鼠往上
        };
    }
    window.addEventListener("scroll",navSlide,false);//監聽滑棒
});//滑動功能
$(document).ready(function(){
    $('.btn_2').click(function(){
        $('.input').show();
    });
    $('.closeBtn').click(function(){
        $('.input').hide();
    });
    $("#monday").click(function(){
        $("#monday").remove();
        $(".monday_2").show();
    });
});//測試

$(document).ready(function(){
    function MonDay(){
        var toDay_1 = new Date();//將日期存入變數
        for (i=0;toDay_1.getDay() != 1;i++){//運算到找到禮拜一為止
            var i_2=24;//一天24小時
            toDay_1.setHours(toDay_1.getHours()-24);//迴圈每跑一次就減去一天
        }
        return toDay_1
    }//找出當周星期一的日期，手輸月分會加一個月，因為系統用陣列記錄月份
    function firstDay(){
        var toDay_2 = new Date();
        var toDay_3 = new Date();
        for(var i=1;toDay_2.getMonth()==toDay_3.getMonth();i++){
            toDay_2.setHours(toDay_2.getHours()-24);
        }
        toDay_2.setHours(toDay_2.getHours()+24);
        return toDay_2
    }//找出當月第一天
    function lestDat(){
        var toDay_2 = new Date();
        var toDay_3 = new Date();
        for(var i=1;toDay_2.getMonth()==toDay_3.getMonth();i++){
            toDay_2.setHours(toDay_2.getHours()+24);
        }
        toDay_2.setHours(toDay_2.getHours()-24);
        return toDay_2
    }//找出當月最後一日
    function yesterday(today,no){
        var today_2 = today.setHours(today.getHours()-no*24);
        alert(today_2);
        return today_2
    }
    for(var i=0;i<=lestDat().getDate()-firstDay().getDate();i++){
        var vDay =new Date(firstDay().setHours(firstDay().getHours()+i*24));
        $("#month").append('<div class=mon id="'+"day"+i+'"></div>');
        $("#day"+i).prepend('<p id="'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'">'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'</p>');
    }

    var cDate=0;
    $("#pgUp").click(function(){
        cDate=cDate-1;
        for(var i_3=0;i_3<7;i_3++) {
            document.getElementById('day' + i_3).innerHTML = "";
        }
        for(var i_3=0;i_3<7;i_3++) {
            var vDay=new Date(MonDay().setHours(MonDay().getHours()+i_3*24+cDate*24*7));
            $("#day"+i_3).prepend('<div id="'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'">'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'</div>');
        }
    });

    $("#pgDn").click(function(){
        cDate=cDate+1;
        for(var i_3=0;i_3<7;i_3++) {
            document.getElementById('day' + i_3).innerHTML = "";
        }
        for(var i_3=0;i_3<7;i_3++) {
            var vDay=new Date(MonDay().setHours(MonDay().getHours()+i_3*24+cDate*24*7));
            $("#day"+i_3).prepend('<div id="'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'">'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'</div>');
        }
    });

});//日期表

//000
