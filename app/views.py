from django.shortcuts import render

# Create your views here.

def component(request):
    return render(request,'component.html')