var width_move = function() {
    $('.video').addClass('video_phone');
    $('.status_backers').addClass('status_backers_phone');
    $('.status_backers_sec').addClass('status_backers_sec_phone');
}//if判斷式的公用部分
var main = function() {
    var flag=0,timer,timer_2;
    $('.logo').hover(function(){
        $('.logo').toggleClass('change');
    });//切換LOGE顏色
    $('.nav').mouseenter(function(){
        clearTimeout(timer_2);
        flag=1;
    });//滑鼠移入ＮＡＶ取消縮回倒數
    $('.nav').mouseleave(function() {
        if ($(document).scrollTop() > 0) {//避免在頂端時縮回
        timer_2 = setTimeout(function () {
            $('.nav').slideUp(500);
            setTimeout(function(){flag=0},500);
        }, 1000);
        }
    });//滑鼠移出時倒數縮回
    var height_1 = $(window).height();//取得視窗取得視窗高度
    var width_2 = $(window).width();   //視窗實際寬度
    if (width_2 < 600){
        $(width_move());
    }
    var scrollTest=function(){
        if($(document).scrollTop()==0){
            $('.nav').addClass('test').slideDown(500);
            clearTimeout(timer_2);}//如果位於頁面頂端，顯示ＮＡＶ
        if(flag==0) {//避免動作重複偵測
            var height_top = $(document).scrollTop();
            timer = setTimeout(function () {
                var height_top_2 = $(document).scrollTop();
                if (height_top_2 - height_top > 0) {//利用１０毫秒差距的高度偵測往上還是往下
                    flag=1;
                    $('.nav').slideUp(500);
                    setTimeout(function(){flag=0},500);//滑動作用期間不偵測滑棒動作
                }
                else if (height_top_2 - height_top < 0) {
                    flag=1;
                    $('.nav').addClass('test').slideDown(500);
                    clearTimeout(timer_2);
                    timer_2=setTimeout(function(){$('.nav').slideUp(500);},3000);//閒置時ＮＡＶ３秒縮回
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

//BUGS  1.滑鼠一開始太上面時，無法鎖定nav　　２.滑鼠鎖定nav，離開時繼續往上滾，會先縮回一次再出現。