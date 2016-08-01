
    <!--

      var arrayIMG = new Array();
        arrayIMG[0]="space.jpg";
        arrayIMG[1]="splash.jpg";
        arrayIMG[2]="lawbook2.jpg";
        arrayIMG[3]="mountain.jpg";
        arrayIMG[4]="nature2.jpg";
        arrayIMG[5]="night.jpg";



        function natureBreak(imgAr, path){

                path = path || 'static/images/nature/'
                var num = Math.floor(Math.random()*imgAr.length);
                var img = imgAr[num];
               return '<img class="img-fluid" src="' +path +img +'" alt ="">';
            
        };


        var clock = setInterval(function(){pictureLoad()},1.2e6);


        function pictureLoad(){

            var imgStr = natureBreak(arrayIMG,"");
            $("#bodyModal").html(imgStr);
            $("#natureModal").modal()
            console.log("success!")

        };


function stopClock(){

            clearInterval(clock);
        }

function countdown( elementName, minutes, seconds )
{

    var element, endTime, hours, mins, msLeft, time;

    function twoDigits( n )
    {
        return (n <= 9 ? "0" + n : n);
    }

    function updateTimer()
    {
        msLeft = endTime - (+new Date);
        if ( msLeft < 1000 ) {
            $("#natureModal").modal("toggle");
        } else {
            time = new Date( msLeft );
            hours = time.getUTCHours();
            mins = time.getUTCMinutes();
            element.innerHTML = (hours ? hours + ':' + twoDigits( mins ) : mins) + ':' + twoDigits( time.getUTCSeconds() );
            setTimeout( updateTimer, time.getUTCMilliseconds() + 500 );
        }
    }

    element = document.getElementById( elementName );
    endTime = (+new Date) + 1000 * (60*minutes + seconds) + 500;
    updateTimer();
}
document.getElementById("countdown").style.color ="#1B232F";
document.getElementById("countdown").style.fontFamily ="Verdana, Arial, sans-serif";
document.getElementById("countdown").style.fontSize="18px";
document.getElementById("countdown").style.fontWeight="bold";
document.getElementById("countdown").style.textDecoration="none";


    -->
