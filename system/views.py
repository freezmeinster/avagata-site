from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post,Kategori,Komentar
from blog.forms import KategoriForm

def index(request):
	
	return render_to_response('system/dashboard.html')

def post(request):
	
	return render_to_response('system/dashboard.html',{
		'url'  :  'post',
	})

def kategori(request):
	kategori = Kategori.objects.all()
	form = KategoriForm
	success = False 
	
	if request.method == 'POST' :
		form = KategoriForm(request.POST)
		if form.is_valid :
			form.save()
			success = True
		
	return render_to_response('system/kategori/index.html',{
		'url' 		: 'kategori',
		'kategori'  :  kategori,
		'form' 		:  form,
		'success'	:  success,
	},context_instance=RequestContext(request))
