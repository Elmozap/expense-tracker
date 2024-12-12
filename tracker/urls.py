from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
]

from django.urls import include, path

urlpatterns = [
    path('', include('tracker.urls')),
]