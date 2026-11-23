from django.shortcuts import render

def index(request):
    return render(request, 'app_Vica/index.html')