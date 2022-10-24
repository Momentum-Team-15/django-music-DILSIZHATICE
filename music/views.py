from django.shortcuts import redirect, render, redirect,  get_object_or_404
from django.utils import timezone
from music.forms import AlbumForm
from music.models import Album

# Create your views here.
def index (request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def album_detail (request, pk):
    albums = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': albums})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect("home")
    else:
        form = AlbumForm()

    return render(request, 'music/create_album.html', {'form': form})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_edit.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect('home')
    return render(request, 'music/album_delete.html')
