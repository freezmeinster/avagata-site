from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from google.appengine.api import users
from blog.models import Post,Kategori,Komentar
from blog.forms import KategoriForm,PostForm
from decorator.ip import get_ip

@login_required
def index(request):
	user = users.get_current_user()	
	url = users.create_login_url("/")
	
	return render_to_response('system/dashboard.html',{
		'user' : user,
		'user_url' : url,
	})

############### View Buat Post  #######################

@login_required
def post(request):
	post = Post.objects.all()
	form = PostForm()
	
	if request.method == 'POST' :
		form = PostForm(request.POST)
		if form.is_valid :
			form.save()
	
	return render_to_response('system/post/index.html',{
		'url'  :  'post',
		'post' : post ,
		'form' : form ,
	})

@login_required
def post_edit(request,post_id):
	pass
#######################################################

################ View buat Kategori ###################
@login_required
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

@login_required
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

@login_required	
def kategori_hapus(request,kategori_id):
	kat = Kategori.objects.get(id=kategori_id)
	kat.delete()
	return redirect('kategori_index')
####################################################
