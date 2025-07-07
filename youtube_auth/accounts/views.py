from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if Profile.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        if password != confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        token = str(uuid.uuid4())
        Profile.objects.create(user=user, email=email, token=token)

        return redirect(f'/verify/{token}')

    return render(request, 'register.html')

def verify(request, token):
    try:
        profile = Profile.objects.get(token=token)
        profile.is_verified = True
        profile.save()
        return render(request, 'verify.html', {'msg': 'Account Verified Successfully'})
    except:
        return render(request, 'verify.html', {'msg': 'Invalid token'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # or use request.GET.get('next', 'dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
