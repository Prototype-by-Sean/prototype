
//var timer;
$(document).ready(function(){
                $('.learnmore').hover(
                    function(){
                        $('span',this).fadeIn(500)
                    },
                    function(){
                        $('span',this).fadeOut()
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
    var flag=0,timer;                           //用一個變數flag來手控navbar的狀態,flag=0代表bar收起,flag=1代表放下,
                                                // 避免addEventListener監聽連續滾動後navbar抽蓄行為

    <!--以下功能為"不論再頁面的何處,只要滾輪往上滾,navbar就要在螢幕頂端滑下,若使用者不需要,三秒後自動收回"-->

    var height_top = $(document).scrollTop()                        //上一次滾輪停止的終點,儲存作為滾動時的開始位置
    var height_top_2 = 0;                                           //同上,結束位置,此變數再下面動作為即時更新
    var navSlide = function(){                                      //把功能存到變數navSlide裡面,為了addEventListener觸發用
                        if(flag==0 || flag==1) {                    //避免動作重複偵測,對應flag2(除非不給偵測)否則都要跑下面的if
                            height_top_2 = $(document).scrollTop(); //當if成立時把目前終點位置存入height_top_2
                            //此段針對不同瀏覽器而設計;因為在監聽滾輪時,Chrome偵測滾輪停止後的位置,Firefox偵測滾輪啟動時的位置
                            if (height_top_2 - height_top > 0) {
                                flag=2;                             //避免height_top_2再被偵測
                                $('.nav').slideUp(200);             //往上縮回
                                setTimeout(function(){
                                    flag=0;
                                    height_top = $(document).scrollTop();   //把目前終點位置存入height_top_2
                                },200);                                     //滑動作用期間不偵測滑棒動作
                            }
                            else if (height_top_2 - height_top < 0 && flag==0) {//<0表示往上,而且flag為收起狀態
                                flag=1;
                                $('.nav').addClass('navSlide').slideDown(200);
                                //此時令flag=1,然後讓增加navSlid這個class讓其存在於目前畫面頂端,用css隱藏起來,再用slide讓他滑下
                                setTimeout(function(){
                                    flag=0;
                                    height_top = $(document).scrollTop();
                                },200);
                                clearTimeout(timer);                //如過滑鼠繼續往上，停止縮回計時
                                timer=setTimeout(function(){
                                    $('.nav').slideUp(200);
                                },3000);                            //閒置時NAV３秒縮回
                                setTimeout(function(){
                                if ($(document).scrollTop()==0){
                                    clearTimeout(timer);
                                    $('.nav').addClass('navSlide').slideDown(500);
                                    setTimeout(function(){flag=0},500);
                                }
                                },200);
                        }
                        }
                        if($(document).scrollTop()==0){         //如果位於頁面頂端"scrollTop()==0",然後再滑下
                            clearTimeout(timer);                //先取消"兩秒後自動收回"的倒數計時
                            $('.nav').slideDown(500);           //然後讓nav滑下
                            setTimeout(function(){flag=1},500); //500MS之後flag=1
                        }
                    };
    window.addEventListener("scroll",navSlide,false);   //監聽JQ事件"scroll"若是發生,就觸發navSlide這個功能

    <!--以下功能為"當滑鼠移到navbar上面時,它不可以縮回去"-->
    $('.nav').mouseenter(function(){            //滑鼠進入nav就取消time_2的倒數計時
        clearTimeout(timer);                    //time是用來倒數計時navbar兩秒後自動收回用的變數
        flag=1;                                 //然後手動把flag調整為放下
    });
    $('.nav').mouseleave(function(){
        if ($(document).scrollTop()>0){         //滑鼠移開nav,且如果scrollTop() > 0表示目前頁面不再頂端,
            timer = setTimeout(function(){      //time_2開始倒數1000毫秒後收起nav,並手動把flag 狀態調為收起
                $('.nav').slideUp(200);
            },1000);
            flag=0;
        }
    });

});
<!--navbar功能結束-->


//$(document).ready(main);