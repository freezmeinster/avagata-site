from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index',name="blog_index" ), 
    url(r'^post/(?P<post_id>\d+)/$','blog.views.post_view',name="post_blog_view" ), 
    
    url(r'^kategori/(?P<kategori_id>\d+)/$','blog.views.kategori_index',name="kategori_blog_index" ),
    
    url(r'^static/about/?$','blog.views.about',name="blog_about" ),
    url(r'^system/',include('system.urls')),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
)
