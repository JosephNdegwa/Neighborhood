from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .emails import send_welcome_email
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateProfileForm, BusinessForm, NeighborhoodForm,PostForm
from .models import Profile, Business, Neighborhood,Post,NewMemberMail
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
            user = authenticate(username=username, password=password)
            login(request, user)
            print("signed up")
            return redirect('homepage')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

def hoods(request):
    my_hoods = Neighborhood.objects.all()
    my_hoods = my_hoods[::-1]
    params = {
        'my_hoods': my_hoods,
    }
    return render(request, 'my_hoods.html', params)


def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form': form})


def single_hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighborhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)


def hood_members(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighborhood=hood)
    return render(request, 'members.html', {'members': members})


def create_post(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


def profile(request):
    hoods = Neighborhood.objects.filter(user=request.user)
    return render(request, 'profile.html',{"hoods":hoods})


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})


def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any category"
    return render(request, "results.html")



def hood_member(request):
    name = request.POST.get('username')
    email = request.POST.get('email')

    recipient = NewMemberMail(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to Neighborhood'}
    return JsonResponse(data)



