from django.contrib import admin
from django.urls import path, include

import account.urls 
import immiprocess.urls 

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('home/',include('immiprocess.urls'))
]
