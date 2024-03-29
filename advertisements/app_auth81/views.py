from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ExetendedUserCreationForm

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_autenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if login_required.method == 'POST':
        form = ExetendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = ExetendedUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'app_auth81/register.html', context)