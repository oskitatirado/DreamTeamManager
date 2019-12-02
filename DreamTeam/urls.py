#encoding:utf-8
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index',name='index'),
    url(r'^signup/(?P<ligaId>\d+)/$','main.views.signup', name='signup'),
    url(r'^populate', 'main.views.populateDB'),
    url(r'^privada', 'main.views.privada',name='privada'),
    url(r'^listaAgenteLibre', 'main.views.agentesLibres',name='lista'),
    url(r'^addUsuario', 'main.views.add'),
    url(r'^create/alineacion', 'main.views.form_alin',name='alineacionList'),
    url(r'^clasificacion', 'main.views.clasificacion',name='clasificacionList'),
    url(r'^semanal', 'main.views.clasificacionSemanal'),
    url(r'^suplente', 'main.views.suplente'),
    url(r'^downloadCSV', 'main.views.dowmload_csv'),
    url(r'^crearMercado', 'main.views.crear_mercado'),
    url(r'^mercado','main.views.mercado',name='mercadoDeJugadores'),
    url(r'^crearPuja/(?P<jugadorId>\d+)/$','main.views.crearPuja'),
    url(r'^vender/(?P<jugadorId>\d+)/$','main.views.vender'),
    url(r'^quitarMercado/(?P<jugadorId>\d+)/$','main.views.quitarMercado'),
    url(r'^valor', 'main.views.darValor'),
    url(r'^ofrecer', 'main.views.ofrecer'),
    url(r'^puja/$','main.views.puja'),
    url(r'^addMercado/$','main.views.addMercado'),
    url(r'^guardarAlineacion', 'main.views.guardarAlineacion'),
    url(r'^liga', 'main.views.liga'),
    url(r'^remUsuario', 'main.views.rem'),
    url(r'^registroLiga', 'main.views.registroLiga',name='registroLiga'),
    url(r'^tipoLiga/$','main.views.tipoLiga'),
    url(r'^puntuacion/$', 'main.views.listing',name='listinga'),
    url(r'^cargarPuntuacion', 'main.views.cargarPuntuacion'),
    url(r'^alinSemanal', 'main.views.guardar_alin_semanal'),
    url(r'^misPujas', 'main.views.misPujas',name='misPujas'),
    url(r'^aceptarPuja/(?P<pujaId>\d+)/$','main.views.aceptarPuja'),
    url(r'^rechazarPuja/(?P<pujaId>\d+)/$','main.views.rechazarPuja'),
    url(r'^login', login,{'template_name':'login.html'},name='login'),
    url(r'^logout', logout_then_login,name='logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

