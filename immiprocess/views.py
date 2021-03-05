from django.shortcuts import render
from account.views import login_page
from django.decorators import login_requiered

def homepage(req):
	context = {}
	return render(req,'main/homepage.html',context)

#@login_requiered(login_url='login')
def service_params(req):
	context = {}
	return render(req,'process/manuparams.html',context)
