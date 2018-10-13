from rest_framework import serializers
from blog.models import Publicacion, Cuento

class PublicacionSerializer(serializers.HyperlinkedModelSerializer):
    cuentos = serializers.HyperlinkedRelatedField(view_name='cuento-detail', read_only=True, many=True)
    class Meta:
        model = Publicacion
        fields = ('url', 'titulo', 'foto', 'cuentos')

class CuentoSerializer(serializers.HyperlinkedModelSerializer):
    # publicacion = serializers.HyperlinkedRelatedField(view_name='publicacion-detail', read_only=True)

    class Meta:
        model = Cuento
        fields = ('url', 'publicacion', 'titulo', 'texto')