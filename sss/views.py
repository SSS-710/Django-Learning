from django.shortcuts import render
from django.http import HttpResponse
from.models import ChaiVarity

def sss(request):
def all_chai(request):
    chais = ChaiVarity.objects.all
    return render(request, 'chai/all_chai.html')
    return HttpResponse("SSS Page")