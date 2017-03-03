from django.conf.urls import patterns, include, url
from apps.activo.views import activo_mostrar, activo_nuevo, activo_editar

urlpatterns = patterns('',
    url(r'^$', activo_mostrar, name="mostrar"),
    url(r'^nuevo$', activo_nuevo, name="nuevo"),
    # url(r'^activo_editar/(?P<id_activo>\d+)/$', include('activofijo.urls', namespace='activo')),
    #url(r'^activo_editar/(?P<id_activo>\d+)/$', activo_editar, name='activo_editar'),
)