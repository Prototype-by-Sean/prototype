$(function () {
        $('#connect_websocket').click(function () {
            if(window.s){
                window.s.close()
            }
            var s = new WebSocket("ws://" + window.location.host + "/match/echo");
            s.onopen = function () {
                console.log('WebSocket open');
            };
            s.onmessage = function (e) {
                console.log('message: ' + e.data);
                $('#messagecontainer').prepend('<p>' + e.data + '</p>');
            };
            window.s = s;
        });
        $('#send_message').click(function () {
            if(!window.s){
                alert("Please connect server.");
            }else{
                window.s.send($('#message').val());
            }
        });
        $('#close_websocket').click(function () {
            if(window.s){
                window.s.close();
            }
        });

    });
