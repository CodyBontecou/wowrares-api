''' backend application url patterns '''

from django.urls import path

from .views import home, zone_view, mob_view, update

urlpatterns = [
    path('', home, name='home'),
    path('update/', update, name='update'),
    path('zone/<zone>/', zone_view, name='zone'),
    path('zone/<zone>/mob/<mob>/', mob_view, name='mob')
]
