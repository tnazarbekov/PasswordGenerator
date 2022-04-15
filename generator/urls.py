from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('about_us', views.about_us, name='about_us'),
    path('huston', views.huston, name='huston')
]
