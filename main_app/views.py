from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Wish

def home(request):
    wishes = Wish.objects.all()
    return render(request, 'home.html', {
        'wishes': wishes,
        })

def wishes_index(request):
    wishes = Wish.objects.all()
    return render(request, 'wishes/index.html', {'wishes': wishes})

def wishes_detail(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    return render(request, 'wishes/detail.html', { 
        'wish': wish,
    })

class WishCreate(CreateView):
    model = Wish
    fields = ['wish']

class WishUpdate(UpdateView):
    model = Wish
    fields = ['wish']

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'