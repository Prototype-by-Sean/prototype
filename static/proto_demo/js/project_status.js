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

<!--navbar功能開始-->
$(document).ready(function(){
    var flag=0,timer;                           //用一個變數flag來手控navbar的狀態,flag=0代表bar收起,flag=1代表放下,
                                                // 避免addEventListener監聽連續滾動後navbar抽蓄行為

    $('.logo').hover(function(){                //切換LOGE顏色
        $('.logo').toggleClass('change');
    });

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
    $(".switch").mouseenter(
        function(){
            timer5 = setTimeout(function() {
                    $(".test").show(200)
                }
                ,500)

                }
    );

    $(".switch").mouseleave(
        function(){
            clearTimeout(timer5);
            timer6 = setTimeout(function(){
                $(".test").hide(200)
            },600)

        }
    );

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
    var thisMonth = lestDat().getDate();
    for(var i=0;i<=lestDat().getDate()-firstDay().getDate();i++){
        var vDay =new Date(firstDay().setHours(firstDay().getHours()+24));
        $("#month").append('<div class=mon id="'+"day"+i+'"></div>');
        $("#month").on('ready','#day1',
            function(){
            alert("12");
            $("#day"+i).prepend('<div id="'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'">'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'</div>');
        }
        );
    }
    setTimeout(function(){for(var i_3=0;i_3<=30;i_3++){
        var vDay =new Date(firstDay().setHours(firstDay().getHours()+i_3*24));
        $("#day"+i_3).prepend('<div id="'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'">'+vDay.getMonth()+"M"+vDay.getDate()+"D"+'</div>');
    };},100);
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
