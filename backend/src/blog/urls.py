from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^publicaciones/$', views.PublicacionList.as_view(), name='publicacion-list'),
    url(r'^publicaciones/(?P<pk>[0-9]+)/$', views.PublicacionDetail.as_view(), name='publicacion-detail'),
    url(r'^cuentos/$', views.CuentoList.as_view(), name='cuento-list'),
    url(r'^cuentos/(?P<pk>[0-9]+)/$', views.CuentoDetail.as_view(), name='cuento-detail'),

]