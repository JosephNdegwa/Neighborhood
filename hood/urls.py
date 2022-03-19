from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

from hood import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    


]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)