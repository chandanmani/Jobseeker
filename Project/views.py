from django.shortcuts import render,redirect
from .forms import CustommUser
from  django.contrib.auth  import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

 



def Main(request):
    return render(request,"index.html")

def register(request):
    message=""
    form=CustommUser()
    if request.method=="POST":
        form=CustommUser(request.POST)
        if form.is_valid():
            form.save()
            message="Register Done Successfully"
        else:
             message="Failed"
    return render(request,'register.html',{"form":form,"message":message})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/Job/viewjob")  # Redirect to dashboard on successful login
        else:
            # Handle invalid login credentials
            return render(request, "login.html", {"message": "Invalid username or password."})
    else:
        return render(request, "login.html")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

from django.core.mail import send_mail
# from django.template.loader import render_to_string

# views.py

from django.core.mail import send_mail
from django.shortcuts import render

def send_custom_email(request):
        if request.method == 'GET': 
             subject = 'Applying Job'
             message = 'Thankyou for Applying Job at Portal '
             reciept=request.user.email
             print(reciept)
             send_mail(subject, message, 'Chandanmani118@gmail.com',[reciept,])
        return render(request, "SendEmail.html",{"message":message})


    


