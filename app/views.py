from django.shortcuts import render
from .models import *

# Create your views here.
def Registerpage(request):
    return render(request,"register.html")


def UserRegister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user= User.objects.filter(Email=email)

        if user:
            message="User Already Exist"
            return render(request,"register.html",{'msg':message})
        
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,
                                    Contact=contact,Password=password)
                message= "User Register Successfully"
                return render(request, "login.html",{'msg':message})
            
            else:
                message= "Password and Cpassword are dosenot match"
                return render(request, "register.html",{'msg':message})
#login view

def Loginpage(request):
    return render(request,'login.html')


#Login User

def Loginuser(request):
    if request.method=='POST':
        email = request.POST["email"]
        password= request.POST["password"]
 #checking the email id with database

        user=User.objects.get(Email=email)
        if user:
            if user.Password==password:
                #we are getting user data in session
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request, 'home.html')
            
            else:
                message= "Password does not match"
                return render(request,'login.html',{'msg':message})
        else:
            message="User does not exist"
            return render(request, 'register.html',{'msg':message})

def DirectLogin(request):
    return render(request,'login.html')
