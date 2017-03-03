from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from activofijo.views import index

urlpatterns = patterns('',
	url(r'^$', login, {'tamplate_name':'index.html'}, name="login"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activo/', include('apps.activo.urls', namespace="activo")),
    url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),
)