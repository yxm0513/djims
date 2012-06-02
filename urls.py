from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djims.views.home', name='home'),
    # url(r'^djims/', include('djims.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'show_indexes': True}, name='static'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'product.views.home', name='home'),
    url(r'^home/', 'product.views.home', name='home'),
    url(r'^index/', 'product.views.template', name='template'),
    url(r'^test/', 'product.views.test', name='test'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout',{'template_name': 'logout.html'}, name='logout'),
)
