from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'immiprocess'

urlpatterns = [
	path('global/info/', views.global_info,name='global_info'),
	path('global/service/',views.service, name='service')
]