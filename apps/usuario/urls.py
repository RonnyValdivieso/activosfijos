from django.conf.urls import patterns, include, url
from apps.usuario.views import RegistroUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^registrar/', login_required(RegistroUsuario.as_view()), name="registrar"),
    # url(r'^editar/(?P<id_user>\d+)/$', login_required(editar), name='editar'),
    # url(r'^eliminar/(?P<id_user>\d+)/$', login_required(eliminar), name='eliminar'),
)