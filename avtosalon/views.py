from django.shortcuts import render
from django.shortcuts import redirect
from .models import Avtosalon
# Create your views here.
def index(request):
    avtosalons = Avtosalon.objects.all()
    context = {
        "avtosalons": avtosalons,
    }
    return render(request, 'index.html', context)
def detail(request, id):
    avtosalon = Avtosalon.objects.get(id=id)
    context = {
        "avtosalon": avtosalon,
    }
    return render(request, 'detail.html', context)

def create(request):
    if request.method == "POST":
        car_name = request.POST['car_name']
        color = request.POST['color']
        year = request.POST['year']
        brand = request.POST['brand']
        country = request.POST['country']
        type = request.POST['type']
        price = request.POST['price']

        avtosalon = Avtosalon.objects.create(
            car_name=car_name,
            color=color,
            year=year,
            brand=brand,
            country=country,
            type=type,
            price=price
        )
        avtosalon.save()
        return redirect('index' )
    return render(request, 'create.html')

def update(request, id):
    avtosalon = Avtosalon.objects.get(id=id)
    if request.method == "POST":
        avtosalon.car_name = request.POST['car_name']
        avtosalon.color = request.POST['color']
        avtosalon.year = request.POST['year']
        avtosalon.brand = request.POST['brand']
        avtosalon.country = request.POST['country']
        avtosalon.type = request.POST['type']
        avtosalon.price = request.POST['price']
        avtosalon.save()
        return redirect('index')
    return render(request, 'update.html', {'avtosalon': avtosalon})
def delete(request, id):
    avtosalon = Avtosalon.objects.get(id=id)
    avtosalon.delete()
    return redirect('index')
