


function checkEmpty(form){
    if(form.name1.value == "a" && form.pass1.value == "b"){
        alert("ItWorks");
    }else
    {
        alert("Thats wrong fam");
    }
}

// To
document.getElementById("fromSpotify").addEventListener("click", function(){
    checkEmpty();
});
document.getElementById("fromApple").addEventListener("click", function(){
  alert("From apple");
});
document.getElementById("fromGoogle").addEventListener("click", function(){
  alert("From google");
});

// From
document.getElementById("toSpotify").addEventListener("click", function(){
  alert("To spotify");
});
document.getElementById("toApple").addEventListener("click", function(){
  alert("To apple");
});
document.getElementById("toGoogle").addEventListener("click", function(){
  alert("To google");
});
