from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Albums


def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})