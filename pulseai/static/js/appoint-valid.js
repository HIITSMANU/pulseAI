function appvalidate(e){
    let mobile = document.querySelector("#mobile").value;

    let error = false

    if(mobile == "" || mobile == null){
        document.querySelector("#mobile").style.border = "1px solid red"
        document.querySelector("#mobileError").innerHTML = "Please enter your mobile number"
    }

    if(mobile.length < 10){
        document.querySelector("#mobile").style.border = "1px solid red"
        document.querySelector("#mobileError").innerHTML = "Please enter 10 digit mobile number"
    }
    else{
        document.querySelector("#mobile").style.border = "1px solid green"
        document.querySelector("#mobileError").innerHTML = " "
    }


    if(error){
        e.preventDefault();
    }



}