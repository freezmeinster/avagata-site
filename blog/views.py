from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.models import Post,Kategori,Komentar

def index(request):
	kat = Kategori.objects.filter(status='AKTIF')
	post = Post.objects.filter(status='POST')	
	paginator = Paginator(post, 8) # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('halaman', '1'))
	except ValueError:	
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)

	
	return render_to_response('blog/index.html',{
		'kategori' : kat,
		'post' : posts,
	})
	
def kategori_index(request,kategori_id):
	pass	
	
def about(request):
	return render_to_response('blog/index.html')

def post_view(request,post_id):
	pass	
