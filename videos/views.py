from django.shortcuts import get_object_or_404, render

from videoplatform.models import Video

# Create your views here.

def videoDetail(request, video):
    video = Video.objects.filter(title=video)
    print(video)
    return render(request, 'video.html', {'video': video})