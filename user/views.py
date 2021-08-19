from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from .models import LoggedIn

@login_required(login_url='login')
def index(request):
    template_name = 'user/index.html'
    return render(request, template_name)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            x = LoggedIn.objects.create(name = request.user.username, is_logged_in = True )
            print(x)
            u = User.objects.all()
            for i in u:
                if i.username != x.name:
                    print(i)
            return redirect('index')
        else:
            messages.warning(request, 'Username or Password are not verified')
            return redirect('login')
    return render(request, 'user/login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm
        if  request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.warning(request, 'Thank You for registering with us !!!!')
                return redirect('index')
        return render(request, 'user/register.html', {'form':form})
