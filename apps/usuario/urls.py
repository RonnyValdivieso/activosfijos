from django.conf.urls import patterns, include, url
from apps.usuario.views import listar, crear, editar, eliminar

urlpatterns = patterns('',
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/', crear, name="nuevo"),
    url(r'^editar/(?P<id_usuario>\d+)/$', editar, name='editar'),
    url(r'^eliminar/(?P<id_usuario>\d+)/$', eliminar, name='eliminar'),
)