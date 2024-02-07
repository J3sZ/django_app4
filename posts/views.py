from django.shortcuts import render
from  .models import posts
from django.views.generic import ListView
# Create your views here.


class home_page_view(ListView):
    model = posts
    template_name = "home.html"