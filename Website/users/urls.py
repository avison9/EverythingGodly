from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-registration'),
    path('success/', views.success, name='user-success'),
    path('profile/', views.profile, name='profile')
   
   ]