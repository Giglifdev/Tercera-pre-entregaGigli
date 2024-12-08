from django import forms
from .models import Albums, Canciones, Artistas

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ['titulo']

class CancionForm(forms.ModelForm):
    class Meta:
        model = Canciones
        fields = ['titulo']

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artistas
        fields = ['nombre']