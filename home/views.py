from django.shortcuts import render, HttpResponse

from menu.models import menu, promociones

# Create your views here.
def index(request):

    menuFamiliar = menu.objects.filter(tamaño='FA').order_by('id')
    menuIndividual = menu.objects.filter(tamaño='IN').order_by('id')
    promos = promociones.objects.all().order_by('id')


    context = {
        'menuFamiliar': menuFamiliar,
        'menuIndividual': menuIndividual,
        'promos': promos,
    }

    return render(request, 'home/index.html', context)
