from django.shortcuts import render_to_response

def get_ip(func):
	def return_ip(request,*args, **kwargs):
		return func(request, *args, **kwargs)
		
	return render_to_response('system/dashboard.html')
