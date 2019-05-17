from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import routers, serializers, viewsets, generics

from backend.models import Item, Zone, Mob
from backend.views import update


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = '__all__'


class ItemViewSetList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


class ZoneViewSetList(generics.ListAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'id')


class MobViewSetList(generics.ListAPIView):
    queryset = Mob.objects.all()
    serializer_class = MobSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'zone__name')


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api/v1/items/', ItemViewSetList.as_view(), name='items'),
    url(r'api/v1/zones/', ZoneViewSetList.as_view(), name='zones'),
    url(r'api/v1/mobs/', MobViewSetList.as_view(), name='mobs'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('update/', update, name='update'),
    path('admin/', admin.site.urls),
]
