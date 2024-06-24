
function validate(e){
    let fname = document.querySelector("#f_name").value;
    let lname = document.querySelector("#l_name").value;
    let uname = document.querySelector("#u_name").value;
    let email = document.querySelector("#email").value;
    let password = document.querySelector("#pass").value;
    let password2 = document.querySelector("#pass2").value;
    console.log("called");

    let error = false

    if(fname === '' || fname === null){
        document.querySelector("#fname_error").innerHTML = "Please enter your first name";
        document.querySelector("#f_name").style.border = "1px solid red";
        error = true;
    }
    else{
        document.querySelector("#fname_error").innerHTML = " ";
        document.querySelector("#f_name").style.border = "1px solid green";
    }

    if(lname === '' || lname === null){
        document.querySelector("#lname_error").innerHTML = "Please enter your last name";
        document.querySelector("#l_name").style.border = "1px solid red";
        error = true;
    }
    else{
        document.querySelector("#lname_error").innerHTML = " ";
        document.querySelector("#l_name").style.border = "1px solid green";
    }

    if(uname === '' || uname === null){
        document.querySelector("#uname_error").innerHTML = "Please enter your username";
        document.querySelector("#u_name").style.border = "1px solid red";
        error = true;
    }
    else{
        document.querySelector("#uname_error").innerHTML = " ";
        document.querySelector("#u_name").style.border = "1px solid green";
    }

    let emailPattern = /^[a-z]+[a-z0-9\._]{3,}@[a-z]{3,10}\.[a-z\.]{2,8}$/;
    if(email === '' || email === null){
        document.querySelector("#email_error").innerHTML = "please enter your email"
        document.querySelector("#email").style.border = "1px solid red";
        error = true
    }
    else if(!email.match(emailPattern)){
        document.querySelector("#email_error").innerHTML = "please enter valid email"
        document.querySelector("#email").style.border = "1px solid red";
        error = true
    }
    else{
        document.querySelector("#email_error").innerHTML = " "
        document.querySelector("#email").style.border = "1px solid green";
    }

    let validpass = true;

    let passerror = '';

    if(!password.match(/[a-z]/)){
        passerror += 'Password should contain at least one lowercase letter';
        validpass = false
    }
    if(!password.match(/[A-Z]/)){
        passerror += '<br>Password should contain at least one uppercase letter';
        validpass = false
    }
    if(!password.match(/[0-9]/)){
        passerror += '<br>Password should contain at least one digit';
        validpass = false
    }

    if(!password.match(/[!@#%^&*()_+]/)){
        passerror += '<br>Password should contain at least one special character';
        validpass = false
    }

    if(password.length < 8){
        passerror += '<br>Password should be minimum of 8 characters';
        validpass = false
    }

    if(!validpass){
        document.querySelector("#pass_error").innerHTML = passerror
        document.querySelector("#pass").style.border = "1px solid red";
    }
    else{
        document.querySelector("#pass_error").innerHTML = ''
        document.querySelector("#pass").style.border = "1px solid green";
    }

    if(password2 === '' || password2 === null){
        document.querySelector("#pass2_error").innerHTML = "Please enter confirm password"
        document.querySelector("#pass2").style.border = "1px solid red";
        error = true
    }
    else if(password !== password2){
        document.querySelector("#pass2_error").innerHTML = "Password  does not match"
        document.querySelector("#pass2").style.border = "1px solid red";
        error = true
    }
    else{
        document.querySelector("#pass2_error").innerHTML = ''
        document.querySelector("#pass2").style.border = "1px solid green";
    }



    if(error){
        e.preventDefault();
    }
}