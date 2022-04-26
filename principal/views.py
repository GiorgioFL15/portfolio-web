from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'pages/portfolio.html')

def sobre(request):
    return render(request, 'pages/sobre.html')
