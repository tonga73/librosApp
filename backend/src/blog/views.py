from blog.models import *
from blog.serializers import PublicacionSerializer, CuentoSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class PublicacionList(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = Publicacion



class CuentoList(generics.ListCreateAPIView):
    queryset = Cuento.objects.all()
    serializer_class = CuentoSerializer

class CuentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuento.objects.all()
    serializer_class = CuentoSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'publicaciones': reverse('publicacion-list', request=request, format=format),
        'cuentos': reverse('cuento-list', request=request, format=format)
    })