from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Business, Neighborhood, Post

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Enter a valid email address.")
    bio = forms.CharField(max_length=500, label="Neighborhood", help_text="Let us know which is your neighborhood.", widget=forms.Textarea(
            attrs={"placeholder": "Please let us know which neighborhood you live in",}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighborhood')


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
