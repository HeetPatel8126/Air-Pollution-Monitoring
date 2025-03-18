from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'monitoring/Webpages/home.html')

def live_data(request):
    return render(request, 'monitoring/Webpages/Live_Data.html')