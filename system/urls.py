from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('system.views',
	url(r'^$','index',name='system_index'),
)
