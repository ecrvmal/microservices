import requests
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView

from mainapp.models import Phone


class PhoneListView(ListView):
    paginate_by = 10
    model = Phone


def sale_view(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    data = {
        'phone': f'{phone.brand.name} {phone.name}',
        'price': phone.sale_cost,
    }
    requests.post('http://app2:5000/sale/', data=data)
    # requests.post('http://127.0.0.1:5000/sale/', data=data)
    return HttpResponseRedirect('/')


def repair_view(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    data = {
        'phone': f'{phone.brand.name} {phone.name}',
        'price': phone.repair_cost
    }
    requests.post('http://app2:5000/repair/', data=data)
    return HttpResponseRedirect('/')




