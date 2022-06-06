from django.contrib import admin
from django.urls import path
from account.views import *


urlpatterns = [
    path('account/', account_view, name="account"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('must_authenticate/', must_authenticate_view, name='must_authenticate'),
    path('register/', registration_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user_list/', user_list, name='user_list'),
    path('user_list/<int:pk>/delete', user_delete, name='user_delete'),
    path('user_list/<int:pk>/update', user_update, name='user_update'),
]
