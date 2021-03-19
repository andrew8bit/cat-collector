from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# CATS 
def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# 1. make a view function
# 2. make the html page
# 3. add the view to the urls.py inside of main app.urls

# When i go to localhost:8000/contact

# Django => urls => /contact => views.contact (runs function) => templates => contact.html 