from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVarity,Store
from .forms import ChaiVarityform



def sss(request):
    chais = ChaiVarity.objects.all()   # () missing tha
    return render(request, 'sss/sss.html', {'chais': chais})


def chai_detail(request, chai_id):
    return HttpResponse(f"This is chai detail page for chai {chai_id}")


def chai_store_view(request):
    stores = None
    if request.method == 'POST':
    form = ChaiVarityform(request.POST)
    if form.is_vaild():
        chai_variety = form.cleaned_data['chai_varity']
        Store.objects.filter(chai_varieties=chai_variety)
    return render(request, 'sss/chai_stores.html',
    {'stores':stores})