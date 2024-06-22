from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def formdata(request):
    return render(request, 'patient/signup.html')

def signup(request):
    if request.method == "POST":
        fn = request.POST.get("f_name")
        ln = request.POST.get("l_name")
        un = request.POST.get("u_name")
        email = request.POST.get("email")
        pwd = request.POST.get("pass")

        if User.objects.filter(username=un).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email is already taken")    

        else:
            user = User.objects.create_user(
            first_name = fn, last_name = ln, username = un, email = email, password = pwd
        )
            user.save()
            messages.success(request,"Registration Successful")

            print(fn)
    return render(request,'patient/signup.html')    


def signin(request):
    if request.method == "POST":
        username = request.POST.get("u_name")
        password = request.POST.get("pass")

        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Credentials")
        else:
            login(request,user)
            # return render(request,'blog/index.html')
            return redirect('home')
    return render(request, 'patient/signin.html')

def signout(request):
    logout(request)
    return redirect('home')