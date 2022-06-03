from django.http import HttpResponse
from django.shortcuts import redirect, render

from produit.models import Product
from produit.forms import ProductForm
from django.contrib.auth.decorators import login_required
from account.models import Account
# Create your views here.
# liste des produits


@login_required
def produit_list(request):
    user = request.user
    if user.is_authenticated:
        if not user.is_admin:
            produit_List = Product.objects.all()
            return render(request, 'produit/produit_list.html', {'produit_List': produit_List})
        else:
            return redirect('surveys')
    else:
        return redirect('must_authenticate')


# admin can see his list of produits
@login_required
def produit_list_admin(request):
    user = request.user
    if user.is_authenticated:
        if user.is_admin:
            produit_List = Product.objects.filter(author=user)
            return render(request, 'produit/produit_List.html', {'produit_List': produit_List})
        else:
            return redirect('surveys')
    else:
        return redirect('must_authenticate')


@login_required
def Buy(request, id):
    produit = Product.objects.get(id=id)
    if produit.Prix <= request.user.points and produit.Quantite > 0:
        request.user.points -= produit.Prix
        request.user.save()
        produit.Quantite -= 1
        produit.save()
        return render(request, 'produit/Thanks_Buy.html', {'produit': produit})
    else:
        return redirect("surveys")


@login_required
def create_product(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    if user.is_admin:
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            obj.author = author
            obj.save()
            form = ProductForm()

        context['form'] = form

        return render(request, "produit/create_product.html", context)
    else:
        return redirect('produit_list')
