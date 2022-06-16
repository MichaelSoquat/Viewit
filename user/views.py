from re import template
from django.http import HttpResponse
from django.shortcuts import render
from redis import ResponseError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize

# Create your views here.


def register(request):

        email= request.GET['email']
        print(email)
        return render(request,'register.html', {'email': email})