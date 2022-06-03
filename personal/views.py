from operator import attrgetter
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def home_screen_view(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return render(request, 'account/dashboard.html')
        else:
            return render(request, 'survey/list_c.html')
    else:
        return render(request, 'personal/home1.html')
