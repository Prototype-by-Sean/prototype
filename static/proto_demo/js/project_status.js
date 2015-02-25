var width_move = function() {
    $('.video').addClass('video_phone');
    $('.status_backers').addClass('status_backers_phone');
    $('.status_backers_sec').addClass('status_backers_sec_phone');
}//if判斷式的公用部分
var main = function() {
    $('.logo').hover(function(){
        $('.logo').toggleClass('change');
    });//切換LOGE顏色
    $('.nav').mouseenter(function(){clearTimeout(timer_2);});
    $('.nav').mouseleave(function(){timer_2=setTimeout(function(){$('.nav').slideUp(500);},1000);});
    var height_1 = $(window).height();//取得視窗取得視窗高度
    var width_2 = $(window).width();   //視窗實際寬度
    if (width_2 < 600){
        $(width_move());
    }
var flag=0,flag_2=0,timer,timer_2;
    var scrollTest=function(){
        if($(document).scrollTop()==0){
            $('.nav').addClass('test').slideDown(500);
            clearTimeout(timer_2);}
        if(flag==0) {
            var height_top = $(document).scrollTop();
            timer = setTimeout(function () {
                var height_top_2 = $(document).scrollTop();
                if (height_top_2 - height_top > 0 && flag==0) {
                    flag=1;
                    $('.nav').slideUp(500);
                    setTimeout(function(){flag=0},500);
                }
                else if (height_top_2 - height_top < 0 && flag==0) {
                    flag=1;
                    $('.nav').addClass('test').slideDown(500);
                    clearTimeout(timer_2);
                    timer_2=setTimeout(function(){$('.nav').slideUp(500);},3000);
                    setTimeout(function(){flag=0},500);
                }
            }, 10);
        }
    };

window.addEventListener("scroll",scrollTest,false);


    /*25-73概念圖
     if滾輪向上{
     if(現在離頁頂超過20%){
     if(現在是第一次向上滾){
     nav加入以下效果，固定，隱藏(0)，顯示(150)
     紀錄__滾輪正在向上滾
     以下code延遲1500ms(隱藏(150), nav，移除固定，顯示(0),紀錄__滾輪下次算第一次向上滾)
     }
     else if(現在正在向上滾){
     延遲code取消執行
     以下code延遲1500ms(隱藏(150), nav，移除固定，顯示(0),紀錄__滾輪下次算第一次向上滾)
     }
     if(現在正在向上滾){
     }
     }
     }
     else if滾輪往下{}
     */
};
$(document).ready(main);
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