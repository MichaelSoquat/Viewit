from django.conf import settings
from django.shortcuts import render
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache  import cache_page
from django.contrib.auth.decorators import login_required

from .models import Video

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
@login_required(login_url='/login/')
@cache_page(CACHE_TTL)
def allVideos(request):
    videos= Video.objects.all()
    print(videos)
    return render(request, 'index.html', {'videos': videos})