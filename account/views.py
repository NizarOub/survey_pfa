from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.http import HttpResponse
from account.models import Account


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "account/login.html", context)


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return render(request, "account/dashboard.html", {})
        else:
            return redirect("home")
    else:
        return redirect("must_authenticate")


def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, "account/account.html", context)


def must_authenticate_view(request):
    return render(request, "account/must_authenticate.html", {})


def user_list(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            users = Account.objects.all()
            return render(request, "account/user_list.html", {"users": users})
        else:
            return redirect("surveys")
    else:
        return redirect("must_authenticate")


# Admin can delete user from users list
def user_delete(request, pk):
    if request.user.is_authenticated:
        if request.user.is_admin:
            user = get_object_or_404(Account, pk=pk)
            user.delete()
            return redirect("user_list")
        else:
            return redirect("surveys")
    else:
        return redirect("must_authenticate")

