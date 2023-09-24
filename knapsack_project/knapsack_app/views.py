from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item


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
