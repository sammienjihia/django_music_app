from django.http import Http404
from django.shortcuts import render
from .models import Albums


def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Albums.objects.get(pk=album_id)
    except Albums.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})