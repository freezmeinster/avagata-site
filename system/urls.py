from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('system.views',
	url(r'^$', 'index', name='system_index'),
	url(r'^post$', 'post', name='post_index'),
	url(r'^kategori$', 'kategori', name='kategori_index'),
)
