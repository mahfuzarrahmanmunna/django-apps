from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Chai Aur Django Home Page!")
    return render(request, 'website/index.html')
          
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')