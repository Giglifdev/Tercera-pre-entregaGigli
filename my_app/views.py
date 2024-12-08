from django.shortcuts import render, redirect
from .models import Albums, Canciones, Artistas
from .forms import AlbumForm, CancionForm, ArtistaForm

def index(request):
    return render(request, 'index.html')


def crear_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = AlbumForm()
    return render(request, 'album.html', {'form': form})

def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = CancionForm()
    return render(request, 'cancion.html', {'form': form})

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = ArtistaForm()
    return render(request, 'artista.html', {'form': form})



def buscar(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda
    albums = Albums.objects.filter(titulo__icontains=query) if query else []
    canciones = Canciones.objects.filter(titulo__icontains=query) if query else []
    artistas = Artistas.objects.filter(nombre__icontains=query) if query else []
    
    return render(request, 'buscar.html', {
        'albums': albums,
        'canciones': canciones,
        'artistas': artistas,
        'query': query,
    })