from django.urls import path,include
from rest_framework import routers

from .views import *
router = routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    #path('mi_endpoint', mi_endpoint, name='mi_endpoint'),
    #path('encriptar/<str:dato>', encriptar, name='login'),
    path('descargarVideo', descargarVideo, name='descargarVideo'),
    path('descargarAudio', descargarAudio, name='descargarAudio'),
    path('existeVideo', existeVideo, name='existeVideo'),
    path('videoToMp3', videoToMp3, name='videoToMp3'),
    path('videoToMp3V2', videoToMp3V2, name='videoToMp3V2'),
    path('devolverAudio',devolverAudio,name='devolverAudio')
]


