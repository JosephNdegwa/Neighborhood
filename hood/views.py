from django.shortcuts import render

# Create your views here.
def homepage(request):
    title = 'Neighborhood'
    return render(request, 'homepage.html', locals())
