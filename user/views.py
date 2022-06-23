
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render  
from .forms import CustomUserCreationForm  
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.  
  
def register(request):  
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            
            login(request, user)
            return HttpResponseRedirect('/watchit')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = CustomUserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})
    

def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password= request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/watchit')
        else:
            return render(request, 'login.html', {'wrongData': True, 'redirect': redirect})
    return render(request,'login.html', {'redirect': redirect})

def logout_view(request):
    logout(request) 
    return HttpResponseRedirect('/')

    
        