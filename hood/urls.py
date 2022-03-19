from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from hood import views

urlpatterns=[
    path('', views.homepage, name='homepage'),


]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)