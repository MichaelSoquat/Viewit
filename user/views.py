
from django.shortcuts import redirect, render  
from .forms import CustomUserCreationForm  
# Create your views here.  
  
def register(request):  
    if request.method == 'POST':  
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:  
        form = CustomUserCreationForm()  
        context = {  
        'form':form  
        }  
        return render(request, 'register.html', context)  
    return render(request, 'register.html')  
    
        

    
        