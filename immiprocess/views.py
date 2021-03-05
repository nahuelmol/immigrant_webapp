from django.shortcuts import render
from account.views import login_page
from django.contrib.auth.decorators import login_required

#@login_required(login_url='login')
def service(req):
	context = {}
	return render(req,'process/starting_service.html',context)


def global_info(req):
	context = {}
	return render(req,'process/global_info.html',context)
