from django.contrib import admin
from django.urls import path, include
from knapsack_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('knapsack_app.urls')),
    # Add the URL pattern for the update_inventory view
    path('update_inventory/', views.update_inventory, name='update_inventory'),
]
