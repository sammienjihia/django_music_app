from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Albums, Songs


def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except(KeyError, Songs.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "you did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

