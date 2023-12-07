from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect("start_button")
        else:
            return render(request,"login.html",{
                "error":"Try again"
            })
    return render(request,'login.html')



def start_button(request):
    return render(request,'startbutton.html')

# def index(request):
#     return render(request,'index.html')
