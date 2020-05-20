from django.shortcuts import render, HttpResponse

from menu.models import promociones, pizza

# Create your views here.
def index(request):

    menuIzq = pizza.objects.all().order_by('id')[:6]
    menuDer = pizza.objects.all().order_by('id')[6:]
    promos = promociones.objects.all().order_by('id')

    context = {
        'menuIzq': menuIzq,
        'menuDer': menuDer,
        'promos': promos,
    }

    return render(request, 'home/index.html', context)
