from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='home'),
     path('register/', views.register, name='register'),
    path('login/',views.my_login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.request_tracking, name='request_tracking'),
    # path('home/', views.home_view, name='home'),
]   