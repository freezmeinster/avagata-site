from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^$','blog.views.index',name="blog_index" ), 
    url(r'^about/?$','blog.views.about',name="blog_about" ),
    url(r'^system/?$',include('system.urls')),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
)
