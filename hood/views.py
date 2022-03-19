from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
from .forms import SignUpForm
from .models import User, Business, Neighborhood
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'homepage.html', {"neighborhoods":neighborhoods})



def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("handling signup")
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(name=username, password=password)
            login(request, user)
            print("signed up")
            return redirect('homepage')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
