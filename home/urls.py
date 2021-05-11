from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.LoginUser, name="login"),
    path('logout', views.LogoutUser, name="logout"),
    path('signup', views.SignupUser, name="signup"),
    path('social-auth/', include('social_django.urls', namespace='social')), 

]