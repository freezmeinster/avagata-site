from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('system.views',
	url(r'^$', 'index', name='system_index'),
	
	url(r'^post$', 'post', name='post_index'),
	
	
	url(r'^kategori$', 'kategori', name='kategori_index'),
	url(r'^kategori/(?P<kategori_id>\d+)/edit/?$', 'kategori_edit', name='kategori_edit'),
	url(r'^kategori/(?P<kategori_id>\d+)/hapus/?$', 'kategori_hapus', name='kategori_hapus'),
)
