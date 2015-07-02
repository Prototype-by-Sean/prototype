
//var timer;
$(document).ready(function(){
                $('.learnmore').hover(
                    function(){
                        $('span',this).show()
                    },
                    function(){
                        $('span',this).hide()
                    }
                );
                /*
                $('.innerframe').hover(
                    function(){
                        sliderin = $('.description',this);
                        timer = setTimeout(function(){sliderin.slideDown(200);}, 600);
                    },
                    function() {
                        clearTimeout(timer);
                        $('.description',this).slideUp('slow');
                    }
                );
                為豐富版面捨棄這個功能*/
                });

<!--navbar功能開始-->
$(document).ready(function(){
    var flag=0,timer,timer_2;//nav使用變數
    /*
    $('.logo').hover(function(){
        $('.logo').toggleClass('change');
    });//切換LOGE顏色
    */
    $('.nav').mouseenter(function(){
        clearTimeout(timer_2);
        flag=1;
    });//滑鼠移入NAV取消縮回倒數
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
                        }//如果位於頁面頂端，顯示NAV
                        if(flag==0 || flag==1) {//避免動作重複偵測
                            height_top_2 = $(document).scrollTop();
                        if (height_top_2 - height_top > 0) {//往下，利用10毫秒差距的高度偵測往上還是往下
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
                            setTimeout(function(){
                                flag=0;
                                height_top = $(document).scrollTop();
                            },200);
                            clearTimeout(timer_2);//如過滑鼠繼續往上，停止縮回計時
                            timer_2=setTimeout(function(){
                                    $('.nav').slideUp(200);
                            },3000);//閒置時NAV３秒縮回
                        }//滑鼠往上
                        }
                    };
                    window.addEventListener("scroll",navSlide,false);//監聽滑棒
});//滑動功能
<!--navbar功能結束-->


//$(document).ready(main);