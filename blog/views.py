from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product
# Create your views here.
class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name='blog/home.html'
    