from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class Main(ListView):
    model = Product
    template_name = 'main.html'



class BlogDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
