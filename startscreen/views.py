from django.shortcuts import render

# Create your views here.
def startscreen(request):
    return render(request, 'startscreen.html')