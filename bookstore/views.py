from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    book = Book.objects.all()


    context = {
        'book':book,
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request,'login.html')