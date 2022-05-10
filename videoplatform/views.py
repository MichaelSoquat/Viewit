from django.shortcuts import render

# Create your views here.
def allVideos(request):
    return render(request, 'platform.html')