let timer =document.getElementById("timer");


let count= 10;
                                     
function inTOmin(count){
var min = Math.floor(count/60);
 var s = count%60;

return min+":"+s;

}
    

function counter(){
    count--;
    timer.innerHTML=inTOmin(count);
    if(count<1){
       timer.innerHTML= "YOUR TIME IS OUT";
    }

}
setInterval(counter,1000);