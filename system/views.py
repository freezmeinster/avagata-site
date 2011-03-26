from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from blog.models import Post,Kategori,Komentar
from blog.forms import KategoriForm

def index(request):
	
	return render_to_response('system/dashboard.html')

############### View Buat Post  #######################
def post(request):
	
	return render_to_response('system/dashboard.html',{
		'url'  :  'post',
	})

#######################################################

################ View buat Kategori ###################

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

def kategori_edit(request,kategori_id):
	kat = Kategori.objects.get(id=kategori_id)
	katform = KategoriForm(instance=kat)
	success = False
	
	if request.method  == 'POST' :
		katform = KategoriForm(request.POST,instance=kat)
		if katform.is_valid:
			katform.save()
			success = True
			
	return render_to_response('system/kategori/edit.html',{
		'url' 		: 'kategori',
		'kategori' 	: katform,
		'kat' 		: kat,
		'success' 	: success ,
	},context_instance=RequestContext(request))
	
def kategori_hapus(request,kategori_id):
	kat = Kategori.objects.get(id=kategori_id)
	kat.delete()
	return redirect('kategori_index')
####################################################
