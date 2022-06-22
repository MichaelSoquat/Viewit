from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form

from .models import CustomUser  
  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    first_name = forms.CharField(label='First name', min_length=3, max_length=150) 
    last_name = forms.CharField(label='Last name', min_length=3, max_length=150) 
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    
    class Meta:
        model=CustomUser
        fields = 'username','first_name', 'last_name','email', 'password1','password2'
        
    def username_clean(self):  
        username = self.cleaned_data['Username'].lower()  
        new = CustomUser.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['Email'].lower()  
        new = CustomUser.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = CustomUser.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'],
            first_name = self.cleaned_data['first_name'],  
            last_name = self.cleaned_data['last_name'],  
        )  
        return user  
    
    

