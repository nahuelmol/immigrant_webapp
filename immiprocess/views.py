from django.shortcuts import render

def homepage(req):
	context = {}
	return render(req,'main/homepage.html',context)

def service_params(req):
	context = {}
	return render(req,'process/manuparams.html',context)