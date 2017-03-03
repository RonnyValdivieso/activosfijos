from django.conf.urls import patterns, include, url
from apps.activo.views import listar, crear, editar, eliminar

urlpatterns = patterns('',
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/', crear, name="nuevo"),
    url(r'^editar/(?P<id_activo>\d+)/$', editar, name='editar'),
    url(r'^eliminar/(?P<id_activo>\d+)/$', eliminar, name='eliminar'),
)