from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('',views.homepage),
	path('service_params/', views.service_params,name='init_process')
]