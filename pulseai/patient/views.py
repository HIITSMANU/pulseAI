from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

from patient.form import HeartVitalForm
from patient.predict import predict_heart_disease
from patient.models import HeartVital,Appointment

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


@login_required(login_url='/patient/signin')
def take_a_test(request):
    context = {}
    today = timezone.now().date()
    # we are checking if the user passed the request on that particular day
    is_exists = HeartVital.objects.filter(user = request.user , created_at__date = today).count()
    if(is_exists > 0):
        context["error"] = True
    form = HeartVitalForm()
    if request.method == "POST":
        form = HeartVitalForm(request.POST)
        # print(form.data)
        # patient = form.save() to directly save in the database
        patient = form.save(commit=False)
        # prediction
        patient_data= {}
        for k,v in form.data.items():
            patient_data[k] = v
        patient_data.pop('csrfmiddlewaretoken')
        # print(patient_data)
        prediction = predict_heart_disease(patient_data)
        print(prediction)
        context['prediction'] = prediction

        # save to database
        patient.user = request.user
        patient.HeartDisease = prediction.get('class')
        patient.prediction_probability = prediction.get('probability')
        patient.save()
    context['form'] = form # dictionary is inputed
    return render(request,'patient/take_a_test.html',context)

@login_required(login_url='/patient/signin')
def appointment(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        note = request.POST.get('note')

        if Appointment.objects.filter(user=request.user,date=date).exists():
            messages.error(request,f"Appointment for {date} is already done")
        else:
            appointment = Appointment(user = request.user,mobile=mobile, date=date, note=note)    
            appointment.save()
            messages.success(request,f"Appointment for {date} is done")
    appointments = Appointment.objects.filter(user=request.user).order_by("-date")        
    context = {
        'appointments': appointments
    }
    return render(request,'patient/appointment.html',context)

def delete_appointment(request,aid):
    app = Appointment.objects.filter(id=aid).delete()
    if app:
        messages.success(request,"Appointment Deleted")
    else:
        messages.error(request,"Appointment Not Deleted")

    return redirect('appoint')


def update_appointment(request,aid):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        note = request.POST.get('note')

        if Appointment.objects.filter(user=request.user,date=date).exclude(id=aid).exists():
            messages.error(request,f"Appointment for {date} is already done")
        elif Appointment.objects.filter(date=date).count() >=20:
            messages.error(request,f"Appointment for {date} is all booked !! try some other day")

        else:
            appointment = Appointment(id=aid, user = request.user,mobile=mobile, date=date, note=note)    
            appointment.save()
            messages.success(request,f"Appointment Updated")
            return redirect('appoint')
    app = Appointment.objects.get(id=aid)
    context = {
        'appointment':app
    }
    return render(request,'patient/appointment_update.html',context)