from django.shortcuts import render_to_response
from blog.models import Post,Kategori,Komentar

def index(request):
	kat = Kategori.objects.filter(status='AKTIF')
	return render_to_response('blog/index.html',{
		'kategori' : kat,
	})
	
def about(request):
	return render_to_response('blog/index.html')
