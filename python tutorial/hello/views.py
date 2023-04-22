from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
            'name': 'John', 
            'age': 20,
            'hobby': 'Reading',
            'friends': ['Jane', 'Peter', 'Tony']
    }
    return render(request, 'index.html', context)

def counter(request):
    #count the amount of words 
    fulltext = request.GET['num1']
    return render(request, 'counter.html')