from django import forms
from produit.models import Product

# form to add a new product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Nom_Produit', 'Prix', 'Quantite', 'Image']
