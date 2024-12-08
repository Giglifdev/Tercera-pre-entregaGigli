from django.urls import path
from .views import index, crear_album, crear_cancion, crear_artista,buscar
urlpatterns = [
    path('', index, name='index'),
    path('crear-album/', crear_album, name='crear_album'),
    path('crear-cancion/', crear_cancion, name='crear_cancion'),
    path('crear-artista/', crear_artista, name='crear_artista'),
    path('buscar/', buscar, name='buscar'),
 
    
]