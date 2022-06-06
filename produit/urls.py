from django.contrib import admin
from django.urls import path
from produit.views import *

urlpatterns = [
    path('produits/', produit_list, name='produit_list'),
    path('produits/list/', produit_list_admin, name='produit_list_admin'),
    path('produits/<int:id>/', Buy, name='Buy'),
    path('produits/create/', create_product, name='create_product'),
    path('produits/<int:id>/delete/', delete_product, name='delete_product'),
]
