from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):

    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', '12')) # 12 if no info provided

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('Numbers'):
        characters.extend('123456789')

    if request.GET.get('Symbols'):
        characters.extend('!@£$%^&*()_-=+')

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):

    return render(request, 'generator/about.html')