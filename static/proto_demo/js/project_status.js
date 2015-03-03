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

var main = function() {
    var height_1 = $(window).height();//取得視窗取得視窗高度
    var width_2 = $(window).width();   //視窗實際寬度
    if (width_2 < 600){
        $(widthChange());
    }//　切換手機版本
}//主文件

var navSlideEvent = function(){
    var flag=0,timer,timer_2;//nav使用變數
    $('.logo').hover(function(){
        $('.logo').toggleClass('change');
    });//切換LOGE顏色
    $('.nav').mouseenter(function(){
        clearTimeout(timer_2);
    });//滑鼠移入ＮＡＶ取消縮回倒數
    $('.nav').mouseleave(function() {
        if ($(document).scrollTop() > 0) {//避免在頂端時縮回
            timer_2 = setTimeout(function () {
                $('.nav').slideUp(500);
            }, 1000);
        }
    });//滑鼠移出時倒數縮回
    var navSlide = function(){
        if($(document).scrollTop()==0){
            $('.nav').addClass('navSlide').slideDown(500);
            clearTimeout(timer_2);}//如果位於頁面頂端，顯示ＮＡＶ
        if(flag==0) {//避免動作重複偵測
            var height_top = $(document).scrollTop();
            timer = setTimeout(function () {
                var height_top_2 = $(document).scrollTop();
                if (height_top_2 - height_top > 0) {//利用１０毫秒差距的高度偵測往上還是往下
                    flag=1;
                    $('.nav').slideUp(500);//往上縮回
                    setTimeout(function(){flag=0},500);//滑動作用期間不偵測滑棒動作
                }
                else if (height_top_2 - height_top < 0) {
                    flag=1;
                    $('.nav').addClass('navSlide').slideDown(500);
                    setTimeout(function(){flag=0},500);
                    clearTimeout(timer_2);//如過滑鼠繼續往上，停止縮回計時
                    timer_2=setTimeout(function(){$('.nav').slideUp(500);},3000);//閒置時ＮＡＶ３秒縮回
                }//滑鼠往上
            }, 10);
        }
    };//nav滑動功能
    window.addEventListener("scroll",navSlide,false);//監聽滑棒
}//nac滑動功能

var test=function(){
    $('.testBtn').click(function(){
        $('.input').show();
    });
    $('.closeBtn').click(function(){
        $('.input').hide();
    });
    var DateIn=new Date();
    var testText=document.getElementById("test");
    testText.textContent=ToDay(DateIn.getFullYear(),DateIn.getMonth(),DateIn.getDate());
    function ToDay(year,month,day){
        var toDay_1 = new Date(year,month,day);//將日期存入變數
        for (i=0;toDay_1.getDay() != 1;i++){//運算到找到禮拜一為止
            var i_2=i*24;//一天24小時
            toDay_1.setHours(day-i_2);//迴圈每跑一次就減去一天
        }
        return toDay_1
    }//輸入日期會找出當周星期一的日期，手輸月分會加一個月，系統用陣列記錄月份
}//測試區

$(document).ready(main);
$(document).ready(navSlideEvent);
$(document).ready(test);


//BUGS  1.滑鼠一開始太上面時，無法鎖定nav　