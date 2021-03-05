from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'account'

urlpatterns = [
	path('home/', views.homepage,name='homepage'),
	path('register/', views.register_page, name='register'),
	path('login/', views.login_page, name='login')
]
