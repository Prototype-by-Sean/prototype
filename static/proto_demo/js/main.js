
//var timer;

    var main = function() {
/*        $('.innerframe').hover(
            function(){
                sliderin = $('.description',this);
                timer = setTimeout(function(){sliderin.slideDown(200);}, 600);
            },
            function() {
                clearTimeout(timer);
                $('.description',this).slideUp('slow');
            }
        );*/
        //為豐富版面捨棄這個功能

        $('.learnmore').hover(
            function(){
              $('span',this).show()
            },
            function(){
                $('span',this).hide()
            }
        );
    };

$(document).ready(main);