# Defines URL patterns for users
from django.urls import path, re_path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # log out page
    path('logout/', views.logout_view, name = 'logout'),
    # Registration Page
    path('register/', views.register, name = 'register'),
#    path('login/', login, {'template_name': 'users/login.html'},
#            name = 'login'),

#    url(r'^login/$', login, {'template_name': 'users/login.html'},
#        name = 'login'),
]