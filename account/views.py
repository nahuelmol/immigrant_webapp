from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#@login_required(login_url='login')
def register_page(req):
	context = {}
	return render(req,'accounts/register_page.html',context)

def login_page(req):
	context = {}
	return render(req,'accounts/login_page.html',context)

