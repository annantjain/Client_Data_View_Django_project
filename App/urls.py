from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_cust', views.all_cust, name='all_cust'),
    path('add_cust', views.add_cust, name='add_cust'),
    path('filter_cust', views.filter_cust, name='filter_cust'),
    path('remove_cust', views.remove_cust, name='remove_cust'),
    path('remove_cust/<int:cust_id>', views.remove_cust, name='remove_cust'),
    path('is_active', views.is_active, name='is_active'),
    path('is_inactive', views.is_inactive, name='is_inactive'),
    path('is_potential', views.is_potential, name='is_potential'),
    path('previous_cust', views.previous_cust, name='previous_cust'),
    path('contact', views.contact, name='contact')

    # maps the URL '/xxxx' to the view function xxxx() defined in the views.py file
]