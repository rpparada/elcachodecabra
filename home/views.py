from django.shortcuts import render, HttpResponse

from menu.models import promociones, pizza

# Create your views here.
def index(request):

    listacompleta = pizza.objects.all().order_by('id')
    total = listacompleta.count()

    if total%2 == 0:
        menuIzq = listacompleta[:total/2]
        menuDer = listacompleta[total/2:]
    else:
        menuIzq = listacompleta[:total//2+1]
        menuDer = listacompleta[total//2+1:]

    promos = promociones.objects.all().order_by('id')

    context = {
        'menuIzq': menuIzq,
        'menuDer': menuDer,
        'promos': promos,
    }

    return render(request, 'home/index.html', context)
