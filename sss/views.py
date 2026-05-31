from django.shortcuts import render
from django.http import HttpResponse
from.models import ChaiVarity

def sss(request):
    chais = ChaiVarity.objects.all
    return render(request, 'sss/sss.html', {'chais': chais})