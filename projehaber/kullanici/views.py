from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def login_request(request):
    # post request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        #kritere uygun kullanıcı
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            #parola yanlış ise
            return render(request,'kullanici/login.html',{"error":"kullanıcı adı / parola yanlış."})
        
    # get request
    return render(request,'kullanici/login.html')

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,'kullanici/register.html',{"error":"kullanıcı adı kullanılmaktadır"}) 
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,'kullanici/register.html',{"error":"eposta kullanılmaktadır"}) 
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request,'kullanici/register.html',{"error":"parolalar eşleşmiyor."}) 
    return render(request,'kullanici/register.html')

def logout_request(request):
    return redirect("index")