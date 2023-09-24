from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

from django.http import JsonResponse


def ingredient_library(request):
    product_data = {
        'flour': {
            'value': '$2.99',
            'quantity': '500g',
            'weight': '0.5 kg',
        },
        'butter': {
            'value': '$3.49',
            'quantity': '200g',
            'weight': '0.2 kg',
        },
        'sugar': {
            'value': '$1.99',
            'quantity': '1 kg',
            'weight': '1 kg',
        },
    }
    return render(request, 'index.html', {'product_data': product_data})


def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    items = Item.objects.all()
    # Here you can implement the knapsack algorithm and show the result to the user
    context = {'form': form, 'items': items}
    return render(request, 'knapsack_app/index.html', context)
