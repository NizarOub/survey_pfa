from django.contrib import admin
from django.urls import path
from survey.views import *


urlpatterns = [
    path('surveys/', survey_list, name='surveys'),
    path('list/', survey_list_c, name='list'),
    path("surveys/<int:pk>/", detail, name="detail"),
    path('surveys/create/', create, name='create'),
    path('surveys/<int:pk>/edit/', edit, name='edit'),
    path('surveys/<int:pk>/delete/', delete, name='delete'),
    path('surveys/<int:pk>/question/', question_create, name='question-create'),
    path('surveys/<int:survey_pk>/question/<int:question_pk>/option/',
         option_create, name='option-create'),
    path("surveys/<int:pk>/start/", start, name="start"),
    path("surveys/<int:survey_pk>/submit/<int:sub_pk>/",
         submit, name="submit"),
    path("surveys/<int:pk>/thanks/", thanks, name="thanks"),
]
