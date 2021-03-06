from django.contrib import admin
from django.urls import path, include

import account.urls 
import immiprocess.urls 

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls',namespace='home-home')),
    path('account_user/',include('account.urls',namespace='users')),
    path('account_monitor/',include('account.urls',namespace='monitor')),
    path('service/',include('immiprocess.urls', namespace='start'))
]

