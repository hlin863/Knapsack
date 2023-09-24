from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# import JSONResponse
from django.http import JsonResponse


def update_inventory(request):
    if request.method == 'POST':
        # Retrieve the updated values from the POST request
        product_name = request.POST.get('product')
        value = request.POST.get('value')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')

        # You can update the inventory data in your database here
        # For this example, let's assume you have a model named "InventoryItem"

        # First, you need to retrieve the item from the database, possibly by an ID or some unique identifier
        # For demonstration purposes, we assume you have an item with ID 1
        item_id = 1
        try:
            item = Item.objects.get(pk=item_id)
            # Update the item's attributes with the new values
            item.product_name = product_name
            item.value = value
            item.quantity = quantity
            item.weight = weight
            item.save()
        except Item.DoesNotExist:
            # Handle the case where the item doesn't exist
            pass

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Inventory details updated successfully'})

    # Handle GET requests or other methods
    return JsonResponse({'message': 'Invalid request method'})


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
