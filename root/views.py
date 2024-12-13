from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'root/index.html')

def portfolio_details(request):
    return render(request, 'root/portfolio-details.html')

def service_details(request):
    return render(request, 'root/service-details.html')