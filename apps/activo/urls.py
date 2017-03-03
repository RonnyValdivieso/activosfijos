from django.conf.urls import patterns, include, url
from apps.activo.views import listar, crear, editar, eliminar
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(listar), name="listar"),
    url(r'^nuevo/', login_required(crear), name="nuevo"),
    url(r'^editar/(?P<id_activo>\d+)/$', login_required(editar), name='editar'),
    url(r'^eliminar/(?P<id_activo>\d+)/$', login_required(eliminar), name='eliminar'),
)