from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from .models import UserProfile
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import logout

def home_view(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'customers/register.html', {'form': form})

def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile')  # Redirect to profile page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'customers/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')
    
@login_required
def profile(request):
    user_profile = UserProfile.objects.all()
    return render(request, 'customers/profile.html', {'user_profile': user_profile})



@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/submit_request.html', {'form': form})

@login_required
def request_tracking(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customers/request_tracking.html', {'user_requests': user_requests})

# Create your views here.
