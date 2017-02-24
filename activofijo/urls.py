from django.conf.urls import patterns, include, url
from django.contrib import admin
from sistema.views import index, activo_mostrar, activo_nuevo, activo_editar

urlpatterns = patterns('',
    url(r'^home', 'activofijo.views.home', name='home'),
    url(r'^current_datetime', 'activofijo.views.current_datetime', name='current_datetime'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sistema/', index, name='index'),
    url(r'^activo/', activo_mostrar, name='activo_mostrar'),
    url(r'^activo_nuevo/', activo_nuevo, name='activo_nuevo'),
    url(r'^activo_editar/(?P<id_activo>\d+)/$', include('activofijo.urls', namespace='activo')),
    #url(r'^activo_editar/(?P<id_activo>\d+)/$', activo_editar, name='activo_editar'),
)