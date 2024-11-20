from django.shortcuts import render
from .models import Pool

def home(request):
    return render(request, 'pool/home.html')

def about_us(request):
    return render(request, 'pool/about_us.html')

def pool_list(request):
    pools = Pool.objects.all()  # Retrieve all pools from the database
    return render(request, 'pool/pool_list.html', {'pools': pools})
