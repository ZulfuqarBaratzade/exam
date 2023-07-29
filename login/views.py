from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Login_User
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        login_user = Login_User()
        if login_user.username == username and login_user.password == password:
            return redirect('index')
        else:
            # Handle invalid login credentials here (e.g., show an error message)
            pass

    return render(request, 'login.html')
